from models import User
from system import NutritionSystem
from data import DataManager
from food_db import FOOD_DB


def get_float(prompt):
    while True:
        value = input(prompt).replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Invalid number.")


def get_int(prompt):
    while True:
        value = input(prompt).replace(",", ".")
        try:
            return int(float(value))
        except ValueError:
            print("Invalid number.")


def main():
    data = DataManager()

    user = data.load_user("user.csv")

    if user is None:
        print("=== First Time Setup ===")
        name = input("Name: ")
        weight = get_float("Starting weight: ")

        calorie_goal = get_int("Calories goal: ")
        protein_goal = get_int("Protein goal: ")
        carbs_goal = get_int("Carbs goal: ")
        fiber_goal = get_int("Fiber goal: ")

        user = User(
            name, weight,
            calorie_goal,
            protein_goal,
            carbs_goal,
            fiber_goal
        )
    else:
        print(f"Welcome back, {user.get_name()}!")

    system = NutritionSystem(user)

    system.food_tracker.food_log = data.load_food("food.csv")
    system.weight_tracker.weight_log = data.load_weight("weight.csv")

    if system.weight_tracker.weight_log:
        user.update_weight(
            system.weight_tracker.get_latest_weight()
        )

    while True:
        print("\n==== Nutrition Tracker ====")
        print("1. Add food")
        print("2. Add weight")
        print("3. View today")
        print("4. Save & Exit")

        choice = input("Select: ")

        if choice == "1":
            name = input("Food: ").lower()
            portion = get_float("Portion (e.g. 1, 0.5, 2): ")

            if name in FOOD_DB:
                data_food = FOOD_DB[name]
                system.add_food(
                    name,
                    data_food["calories"],
                    data_food["protein"],
                    data_food["carbs"],
                    data_food["fiber"],
                    portion
                )
                print("Added from database.")
            else:
                print("Manual entry:")
                calories = get_int("Calories: ")
                protein = get_int("Protein: ")
                carbs = get_int("Carbs: ")
                fiber = get_int("Fiber: ")

                system.add_food(
                    name, calories, protein, carbs, fiber, portion
                )

        elif choice == "2":
            weight = get_float("Weight: ")
            system.add_weight(weight)

        elif choice == "3":
            system.show_today()

        elif choice == "4":
            data.save_food(system.food_tracker.food_log, "food.csv")
            data.save_weight(system.weight_tracker.weight_log, "weight.csv")
            data.save_user(user, "user.csv")
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()