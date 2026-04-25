import unittest
import os
from models import User, FoodEntry, WeightEntry
from system import NutritionSystem
from data import DataManager


class TestNutritionSystem(unittest.TestCase):

    def setUp(self):
        self.user = User("Test", 70, 2000, 150, 250, 30)
        self.system = NutritionSystem(self.user)
        self.data = DataManager()

        # Clean test files if they exist
        for f in ["test_food.csv", "test_weight.csv", "test_user.csv"]:
            if os.path.exists(f):
                os.remove(f)

    # =========================
    # USER TESTS
    # =========================
    def test_user_goals(self):
        goals = self.user.get_macro_goals()
        self.assertEqual(goals["protein"], 150)
        self.assertEqual(goals["carbs"], 250)
        self.assertEqual(goals["fiber"], 30)

    # =========================
    # FOOD TESTS
    # =========================
    def test_add_food_basic(self):
        self.system.add_food("apple", 100, 1, 20, 3)
        self.assertEqual(len(self.system.food_tracker.food_log), 1)

    def test_portion_scaling(self):
        self.system.add_food("rice", 100, 2, 20, 1, portion=2)

        entry = self.system.food_tracker.food_log[0]

        self.assertEqual(entry.calories, 200)
        self.assertEqual(entry.protein, 4)
        self.assertEqual(entry.carbs, 40)
        self.assertEqual(entry.fiber, 2)

    def test_macro_totals(self):
        self.system.add_food("food1", 100, 10, 20, 5)
        self.system.add_food("food2", 200, 20, 30, 5)

        self.assertEqual(self.system.food_tracker.get_today_calories(), 300)
        self.assertEqual(self.system.food_tracker.get_today_protein(), 30)
        self.assertEqual(self.system.food_tracker.get_today_carbs(), 50)
        self.assertEqual(self.system.food_tracker.get_today_fiber(), 10)

    # =========================
    # WEIGHT TESTS
    # =========================
    def test_weight_update(self):
        self.system.add_weight(68)
        self.assertEqual(self.user.get_weight(), 68)

    def test_weight_change(self):
        self.system.add_weight(70)
        self.system.add_weight(68)

        change = self.system.weight_tracker.get_weight_change()
        self.assertEqual(change, -2)

    def test_empty_weight_change(self):
        change = self.system.weight_tracker.get_weight_change()
        self.assertEqual(change, 0)

    # =========================
    # DATA PERSISTENCE TESTS
    # =========================
    def test_save_and_load_food(self):
        self.system.add_food("apple", 100, 1, 20, 3)

        self.data.save_food(self.system.food_tracker.food_log, "test_food.csv")
        loaded = self.data.load_food("test_food.csv")

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "apple")

    def test_save_and_load_weight(self):
        self.system.add_weight(70)

        self.data.save_weight(self.system.weight_tracker.weight_log, "test_weight.csv")
        loaded = self.data.load_weight("test_weight.csv")

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].weight, 70)

    def test_save_and_load_user(self):
        self.data.save_user(self.user, "test_user.csv")
        loaded_user = self.data.load_user("test_user.csv")

        self.assertEqual(loaded_user.get_name(), "Test")
        self.assertEqual(loaded_user.get_goal(), 2000)
        self.assertEqual(loaded_user.get_macro_goals()["protein"], 150)


if __name__ == "__main__":
    unittest.main()