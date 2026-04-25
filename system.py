from models import FoodEntry, WeightEntry
from factory import TrackerFactory


class NutritionSystem:
    def __init__(self, user):
        self.user = user
        self.food_tracker = TrackerFactory.create_tracker("food")
        self.weight_tracker = TrackerFactory.create_tracker("weight")

    def add_food(self, name, calories, protein, carbs, fiber, portion=1.0):
        self.food_tracker.add_entry(
            FoodEntry(
                name,
                calories * portion,
                protein * portion,
                carbs * portion,
                fiber * portion,
                portion
            )
        )

    def add_weight(self, weight):
        entry = WeightEntry(weight)
        self.weight_tracker.add_entry(entry)
        self.user.update_weight(weight)

    def show_today(self):
        foods = self.food_tracker.get_today_entries()

        total_cal = self.food_tracker.get_today_calories()
        protein = self.food_tracker.get_today_protein()
        carbs = self.food_tracker.get_today_carbs()
        fiber = self.food_tracker.get_today_fiber()

        cal_goal = self.user.get_goal()
        macro_goals = self.user.get_macro_goals()

        print("\n--- Today ---")
        for f in foods:
            print(
                f"{f.name} x{f.portion} - {f.calories:.1f} kcal "
                f"(P:{f.protein:.1f} C:{f.carbs:.1f} F:{f.fiber:.1f})"
            )

        print("\n--- Progress ---")
        print(f"Calories: {total_cal:.1f}/{cal_goal}")
        print(f"Protein: {protein:.1f}/{macro_goals['protein']} g")
        print(f"Carbs: {carbs:.1f}/{macro_goals['carbs']} g")
        print(f"Fiber: {fiber:.1f}/{macro_goals['fiber']} g")

        print("\n--- Remaining ---")
        print(f"Calories left: {cal_goal - total_cal:.1f}")
        print(f"Protein left: {macro_goals['protein'] - protein:.1f}")
        print(f"Carbs left: {macro_goals['carbs'] - carbs:.1f}")
        print(f"Fiber left: {macro_goals['fiber'] - fiber:.1f}")