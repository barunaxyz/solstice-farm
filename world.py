"""world.py — Tile-map world for Solstice Farm.

Manages the 2D grid of tiles including soil states, crop placement,
rendering with camera offset, and collision queries.
"""

from __future__ import annotations

from typing import Optional

import pygame

from camera import Camera
from farming import Crop
from settings import (
    FARM_COLS, FARM_ROWS, FARM_X, FARM_Y,
    MAP_COLS, MAP_ROWS,
    SHOP_X, SHOP_Y, HOUSE_X, HOUSE_Y,
    SOLID_TILES,
    TILE_DIRT, TILE_FENCE, TILE_GRASS, TILE_PATH,
    TILE_PLANTED, TILE_SHOP, TILE_SIZE,
    TILE_TILLED, TILE_TREE, TILE_WATER, TILE_WATERED,
    TILE_HOUSE_DOOR, TILE_HOUSE_WALL,
    WELL_X, WELL_Y,
)
from sprites import get_crop_stages, get_tile, get_image

T = TILE_SIZE

                                   
_TILE_SPRITE = {
    TILE_GRASS: "grass",
    TILE_DIRT: "dirt",
    TILE_TILLED: "tilled",
    TILE_WATERED: "watered",
    TILE_PATH: "path",
    TILE_TREE: "tree",
    TILE_FENCE: "fence",
    TILE_WATER: "water_source",
    TILE_SHOP: "shop",
    TILE_PLANTED: "watered",                                   
    TILE_HOUSE_WALL: "grass",                                 
    TILE_HOUSE_DOOR: "grass",                                 
}


class World:
    """The tile-based game world."""

    def __init__(self) -> None:
        self.cols = MAP_COLS
        self.rows = MAP_ROWS

                               
        self.tiles: list[list[int]] = self._build_map()

                                                      
        self.crops: dict[tuple[int, int], Crop] = {}

                                                                        
                    
                                                                        

    def _build_map(self) -> list[list[int]]:
        """Procedurally generate the farm map."""
        grid: list[list[int]] = []

        for row in range(self.rows):
            line: list[int] = []
            for col in range(self.cols):
                tile = self._classify_tile(col, row)
                line.append(tile)
            grid.append(line)
        return grid

    def _classify_tile(self, col: int, row: int) -> int:
                       
        if HOUSE_X - 1 <= col <= HOUSE_X + 1 and HOUSE_Y - 2 <= row <= HOUSE_Y:
            if col == HOUSE_X and row == HOUSE_Y:
                return TILE_HOUSE_DOOR
            return TILE_HOUSE_WALL

                                                    
        if row == 0 or row == self.rows - 1 or col == 0 or col == self.cols - 1:
            return TILE_TREE
                                              
        if row == 1 or row == self.rows - 2:
            if col < 3 or col > self.cols - 4:
                return TILE_TREE
            return TILE_GRASS
        if col == 1 or col == self.cols - 2:
            return TILE_TREE

                                          
        if (FARM_X <= col < FARM_X + FARM_COLS and
                FARM_Y <= row < FARM_Y + FARM_ROWS):
            return TILE_DIRT

                                   
        if (col == FARM_X - 1 and FARM_Y - 1 <= row <= FARM_Y + FARM_ROWS):
            return TILE_FENCE
        if (col == FARM_X + FARM_COLS and FARM_Y - 1 <= row <= FARM_Y + FARM_ROWS):
            return TILE_FENCE
        if (row == FARM_Y - 1 and FARM_X - 1 <= col <= FARM_X + FARM_COLS):
            if col == FARM_X + FARM_COLS // 2 or col == FARM_X + FARM_COLS // 2 + 1:
                return TILE_PATH                
            return TILE_FENCE
        if (row == FARM_Y + FARM_ROWS and FARM_X - 1 <= col <= FARM_X + FARM_COLS):
            if col == FARM_X + FARM_COLS // 2 or col == FARM_X + FARM_COLS // 2 + 1:
                return TILE_PATH                
            return TILE_FENCE

                      
        if col == WELL_X and row == WELL_Y:
            return TILE_WATER

                      
        if col == SHOP_X and row == SHOP_Y:
            return TILE_SHOP

                                        
                                          
        if col in (FARM_X + FARM_COLS // 2, FARM_X + FARM_COLS // 2 + 1):
            if FARM_Y + FARM_ROWS <= row <= SHOP_Y + 1:
                return TILE_PATH
                           
        if row == SHOP_Y:
            if FARM_X + FARM_COLS // 2 <= col <= SHOP_X:
                return TILE_PATH
        if row == SHOP_Y + 1 and FARM_X + FARM_COLS // 2 <= col <= SHOP_X:
            return TILE_PATH

                                        
        if col in (FARM_X + FARM_COLS // 2, FARM_X + FARM_COLS // 2 + 1):
            if WELL_Y <= row <= FARM_Y - 1:
                return TILE_PATH
                           
        if row == WELL_Y:
            if WELL_X <= col <= FARM_X + FARM_COLS // 2:
                return TILE_PATH
        if row == WELL_Y + 1 and WELL_X <= col <= FARM_X + FARM_COLS // 2:
            return TILE_PATH

                                           
        if (col + row * 7) % 13 == 0 and col > 3 and row > 3:
            if col < FARM_X - 2 or col > FARM_X + FARM_COLS + 2:
                return TILE_TREE

        return TILE_GRASS

                                                                        
                  
                                                                        

    def get_tile(self, col: int, row: int) -> int:
        if 0 <= col < self.cols and 0 <= row < self.rows:
            return self.tiles[row][col]
        return TILE_TREE                         

    def set_tile(self, col: int, row: int, tile_type: int) -> None:
        if 0 <= col < self.cols and 0 <= row < self.rows:
            self.tiles[row][col] = tile_type

    def is_solid(self, col: int, row: int) -> bool:
        return self.get_tile(col, row) in SOLID_TILES

    def pixel_to_tile(self, px: float, py: float) -> tuple[int, int]:
        return int(px // T), int(py // T)

                                                                        
                     
                                                                        

    def can_till(self, col: int, row: int) -> bool:
        return self.get_tile(col, row) == TILE_DIRT

    def till(self, col: int, row: int) -> bool:
        if self.can_till(col, row):
            self.set_tile(col, row, TILE_TILLED)
            return True
        return False

    def can_water_soil(self, col: int, row: int) -> bool:
        tile = self.get_tile(col, row)
        if tile == TILE_TILLED:
            return True
        if tile == TILE_PLANTED:
            crop = self.crops.get((col, row))
            return crop is not None and crop.needs_water
        return False

    def water_soil(self, col: int, row: int) -> bool:
        tile = self.get_tile(col, row)
        if tile == TILE_TILLED:
            self.set_tile(col, row, TILE_WATERED)
            return True
        if tile == TILE_PLANTED:
            crop = self.crops.get((col, row))
            if crop and crop.needs_water:
                crop.water_crop()
                return True
        return False

    def can_plant(self, col: int, row: int) -> bool:
        return self.get_tile(col, row) == TILE_WATERED

    def plant(self, col: int, row: int, crop_type: str) -> bool:
        if self.can_plant(col, row):
            self.set_tile(col, row, TILE_PLANTED)
            crop = Crop(crop_type)
                                                                 
            crop.water_crop()
            self.crops[(col, row)] = crop
            return True
        return False

    def can_harvest(self, col: int, row: int) -> bool:
        crop = self.crops.get((col, row))
        return crop is not None and crop.ready

    def harvest(self, col: int, row: int) -> Optional[tuple[str, int]]:
        """Harvest the crop. Returns (crop_type, value) or None."""
        crop = self.crops.get((col, row))
        if crop and crop.ready:
            result = (crop.crop_type, crop.harvest_value())
            del self.crops[(col, row)]
            self.set_tile(col, row, TILE_DIRT)                 
            return result
        return None

    def is_water_source(self, col: int, row: int) -> bool:
        return self.get_tile(col, row) == TILE_WATER

    def is_shop(self, col: int, row: int) -> bool:
        return self.get_tile(col, row) == TILE_SHOP

    def is_house(self, col: int, row: int) -> bool:
        return self.get_tile(col, row) == TILE_HOUSE_DOOR

                                                                        
            
                                                                        

    def update(self, dt: float, time_fraction: float) -> None:
        """Advance all crop growth."""
        for crop in self.crops.values():
            crop.update(dt, time_fraction)

                                                                        
             
                                                                        

    def draw(self, surface: pygame.Surface, camera: Camera) -> None:
        """Draw all visible tiles and crops."""
        ox, oy = camera.offset

                                      
        start_col = max(0, int(-ox // T))
        start_row = max(0, int(-oy // T))
        end_col = min(self.cols, start_col + surface.get_width() // T + 2)
        end_row = min(self.rows, start_row + surface.get_height() // T + 2)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile_type = self.tiles[row][col]
                sprite_name = _TILE_SPRITE.get(tile_type, "grass")
                tile_surf = get_tile(sprite_name)

                screen_x = col * T + ox
                screen_y = row * T + oy
                surface.blit(tile_surf, (screen_x, screen_y))

                                  
                crop = self.crops.get((col, row))
                if crop is not None:
                    stages = get_crop_stages(crop.crop_type)
                    stage_idx = crop.stage
                    if 0 <= stage_idx < len(stages):
                        surface.blit(stages[stage_idx], (screen_x, screen_y))

                                     
                    if crop.needs_water and not crop.ready:
                                            
                        drop_x = screen_x + T - 10
                        drop_y = screen_y + 4
                        pygame.draw.circle(surface, (80, 160, 240),
                                           (drop_x, drop_y), 4)
                        pygame.draw.circle(surface, (200, 230, 255),
                                           (drop_x - 1, drop_y - 1), 1)

                                       
                    if crop.ready:
                                             
                        import math
                        pulse = abs(math.sin(pygame.time.get_ticks() / 300.0))
                        r = int(3 + pulse * 2)
                        pygame.draw.circle(surface, (255, 220, 50),
                                           (screen_x + T // 2, screen_y + 2), r)

                                                                                              
        if start_row <= HOUSE_Y < end_row and start_col <= HOUSE_X < end_col:
            if not hasattr(self, '_house_scaled'):
                house_img = get_image("rumah.png")
                hw, hh = house_img.get_width(), house_img.get_height()
                                                               
                target_w = T * 3
                scale_f = target_w / hw
                sw = int(hw * scale_f)
                sh = int(hh * scale_f)
                self._house_scaled = pygame.transform.smoothscale(
                    house_img, (sw, sh))
            scaled_img = self._house_scaled
            
            hx_screen = HOUSE_X * T + ox
            hy_screen = HOUSE_Y * T + oy
                                                                                      
            hx = hx_screen + (T // 2) - (scaled_img.get_width() // 2)
            hy = hy_screen + T - scaled_img.get_height()
            surface.blit(scaled_img, (hx, hy))

                                                                     
        if not hasattr(self, '_font_marker'):
            self._font_marker = pygame.font.SysFont(None, 20, bold=True)
            
        markers = [
            (SHOP_X, SHOP_Y, "SHOP"),
            (WELL_X, WELL_Y, "WELL"),
            (HOUSE_X, HOUSE_Y, "HOUSE")
        ]
        
        for mx, my, mtext in markers:
                                                 
            if start_col <= mx < end_col and start_row <= my < end_row:
                screen_x = mx * T + ox
                screen_y = my * T + oy
                
                text = self._font_marker.render(mtext, True, (255, 255, 255))
                bg = pygame.Surface((text.get_width() + 6, text.get_height() + 4))
                bg.fill((0, 0, 0))
                bg.set_alpha(150)
                
                                                                                    
                y_offset = 15 if mtext == "HOUSE" else 4
                
                cx = screen_x + (T - text.get_width()) // 2
                cy = screen_y - text.get_height() + y_offset
                
                surface.blit(bg, (cx - 3, cy - 2))
                surface.blit(text, (cx, cy))
