"""Smoke tests for core Solstice Farm gameplay rules."""

import unittest

from farming import Crop, get_sun_multiplier
from inventory import Inventory
from settings import CROPS, FARM_X, FARM_Y, TILE_DIRT, TILE_PLANTED
from world import World


class InventoryTest(unittest.TestCase):
    def test_buy_and_sell_crop_updates_money_and_counts(self) -> None:
        inventory = Inventory()
        starting_money = inventory.money

        self.assertTrue(inventory.buy_seeds("lettuce", 1))
        self.assertEqual(starting_money - CROPS["lettuce"]["seed_cost"], inventory.money)
        self.assertEqual(6, inventory.seeds["lettuce"])

        inventory.add_harvest("lettuce", 2)
        self.assertTrue(inventory.sell_crop("lettuce", 1, 2.0))

        expected_money = starting_money - CROPS["lettuce"]["seed_cost"] + CROPS["lettuce"]["sell_price"] * 2
        self.assertEqual(expected_money, inventory.money)
        self.assertEqual(1, inventory.get_harvest_count("lettuce"))
        self.assertEqual(CROPS["lettuce"]["sell_price"] * 2, inventory.total_earned)


class FarmingTest(unittest.TestCase):
    def test_crop_waits_for_water_then_becomes_ready(self) -> None:
        crop = Crop("lettuce")

        crop.update(999.0, 0.45)
        self.assertEqual(0.0, crop.progress)
        self.assertTrue(crop.needs_water)

        self.assertTrue(crop.water_crop())
        crop.update(CROPS["lettuce"]["grow_time"], 0.45)

        self.assertTrue(crop.ready)
        self.assertEqual(CROPS["lettuce"]["sell_price"], crop.harvest_value())

    def test_sun_multiplier_is_clamped(self) -> None:
        self.assertEqual(get_sun_multiplier(0.0), get_sun_multiplier(-1.0))
        self.assertEqual(get_sun_multiplier(1.0), get_sun_multiplier(2.0))


class WorldTest(unittest.TestCase):
    def test_till_water_plant_and_harvest_cycle(self) -> None:
        world = World()
        col = FARM_X
        row = FARM_Y

        self.assertEqual(TILE_DIRT, world.get_tile(col, row))
        self.assertTrue(world.till(col, row))
        self.assertTrue(world.water_soil(col, row))
        self.assertTrue(world.plant(col, row, "lettuce"))
        self.assertEqual(TILE_PLANTED, world.get_tile(col, row))

        crop = world.crops[(col, row)]
        crop.progress = 1.0
        crop.ready = True

        self.assertEqual(("lettuce", CROPS["lettuce"]["sell_price"]), world.harvest(col, row))
        self.assertEqual(TILE_DIRT, world.get_tile(col, row))


if __name__ == "__main__":
    unittest.main()
