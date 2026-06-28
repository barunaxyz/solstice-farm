"""settings.py — Global constants and configuration for Solstice Farm."""

                                                                             
         
                                                                             
SCREEN_W = 960
SCREEN_H = 640
TILE_SIZE = 32
FPS = 60

                                                                             
                           
                                                                             
MAP_COLS = 30
MAP_ROWS = 20

                                                           
FARM_X = 6
FARM_Y = 4
FARM_COLS = 12
FARM_ROWS = 8

                             
SHOP_X = 22
SHOP_Y = 9

                              
WELL_X = 4
WELL_Y = 8

                              
HOUSE_X = 12
HOUSE_Y = 3

                                                                             
          
                                                                             
DAY_DURATION = 600.0                                         
PLAYER_SPEED = 130.0                     
STARTING_MONEY = 100
WATER_CAN_MAX = 15
WATER_CAN_START = 15

                                 
GOLDEN_HOUR_START = 0.65                                          
GOLDEN_HOUR_END = 0.80                                          
GOLDEN_HOUR_MULTIPLIER = 2.0                                    

                 
EVENT_INTERVAL_MIN = 45.0                                   
EVENT_INTERVAL_MAX = 90.0                                   
EVENT_DURATION = 15.0                                

                                                                  
                                                        
SUN_GROWTH_SCHEDULE = [
    (0.00, 0.5),                
    (0.15, 0.8),            
    (0.30, 1.2),                 
    (0.45, 1.5),                                      
    (0.60, 1.2),              
    (0.75, 0.8),                
    (0.90, 0.4),                  
    (1.00, 0.2),                          
]

                                                                             
            
                                                                             
TILE_GRASS = 0
TILE_DIRT = 1                                  
TILE_TILLED = 2                 
TILE_WATERED = 3                   
TILE_PATH = 4                    
TILE_TREE = 5                               
TILE_FENCE = 6                      
TILE_WATER = 7                            
TILE_SHOP = 8                          
TILE_PLANTED = 9                       
TILE_HOUSE_DOOR = 10                            
TILE_HOUSE_WALL = 11                          

SOLID_TILES = {TILE_TREE, TILE_FENCE, TILE_HOUSE_WALL}

                                                                             
       
                                                                             
TOOL_HOE = "hoe"
TOOL_WATER = "water_can"
TOOL_SEEDS = "seeds"
TOOL_HANDS = "hands"

TOOLS_LIST = [TOOL_HOE, TOOL_WATER, TOOL_SEEDS, TOOL_HANDS]
TOOL_NAMES = {
    TOOL_HOE: "Hoe",
    TOOL_WATER: "Water Can",
    TOOL_SEEDS: "Seeds",
    TOOL_HANDS: "Harvest",
}

                                                                             
           
                                                                             
CROPS = {
    "lettuce": {
        "name": "Lettuce",
        "grow_time": 40.0,
        "sell_price": 15,
        "seed_cost": 5,
        "stages": 3,
        "water_needed": 1,
        "color": (80, 190, 60),
        "fruit_color": (100, 210, 80),
    },
    "tomato": {
        "name": "Tomato",
        "grow_time": 70.0,
        "sell_price": 35,
        "seed_cost": 12,
        "stages": 4,
        "water_needed": 2,
        "color": (60, 150, 50),
        "fruit_color": (210, 55, 45),
    },
    "corn": {
        "name": "Corn",
        "grow_time": 100.0,
        "sell_price": 60,
        "seed_cost": 20,
        "stages": 4,
        "water_needed": 2,
        "color": (70, 160, 55),
        "fruit_color": (240, 210, 70),
    },
    "sunflower": {
        "name": "Sunflower",
        "grow_time": 120.0,
        "sell_price": 100,
        "seed_cost": 35,
        "stages": 5,
        "water_needed": 3,
        "color": (55, 140, 45),
        "fruit_color": (230, 195, 30),
    },
    "strawberry": {
        "name": "Strawberry",
        "grow_time": 90.0,
        "sell_price": 80,
        "seed_cost": 25,
        "stages": 4,
        "water_needed": 2,
        "color": (65, 155, 50),
        "fruit_color": (220, 40, 50),
    },
    "solstice_bloom": {
        "name": "Solstice Bloom",
        "grow_time": 80.0,
        "sell_price": 200,
        "seed_cost": 50,
        "stages": 5,
        "water_needed": 2,
        "color": (120, 80, 180),
        "fruit_color": (220, 160, 255),
        "special": "solstice_only",                              
    },
}

CROP_TYPES = list(CROPS.keys())

                                                                             
                                       
                                                                             
PAL = {
        
    "bg_dark": (15, 12, 20),
    "bg_panel": (25, 35, 30),
    "text_light": (240, 235, 220),
    "text_gold": (240, 210, 50),
    "text_dim": (150, 145, 130),
    "accent": (100, 200, 80),
    "accent_bright": (140, 240, 100),
    "danger": (220, 60, 50),
    "water_blue": (80, 150, 230),

           
    "grass_a": (90, 165, 65),
    "grass_b": (80, 150, 55),
    "grass_c": (100, 175, 72),
    "dirt": (140, 100, 55),
    "dirt_dark": (110, 75, 40),
    "tilled": (95, 65, 35),
    "tilled_line": (75, 50, 25),
    "watered": (65, 50, 30),
    "path": (175, 165, 145),
    "path_dark": (145, 135, 115),
    "tree_trunk": (100, 70, 35),
    "tree_leaves": (55, 130, 45),
    "tree_leaves_light": (75, 155, 55),
    "fence": (155, 115, 65),
    "fence_dark": (120, 85, 45),
    "water": (70, 140, 210),
    "water_light": (110, 175, 235),
    "shop_wall": (180, 140, 90),
    "shop_roof": (160, 60, 50),

            
    "skin": (240, 200, 160),
    "hair": (100, 65, 30),
    "shirt": (70, 130, 200),
    "pants": (60, 75, 120),
    "hat": (200, 170, 80),
    "hat_band": (160, 60, 50),
}
