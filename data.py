import csv
import os
from datetime import datetime
from models import FoodEntry, WeightEntry, User


class DataManager:

    # ========= FOOD =========
    def save_food(self, food_log, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Name", "Calories", "Protein", "Carbs", "Fiber", "Portion", "Date"]
            )

            for f in food_log:
                writer.writerow([
                    f.name, f.calories, f.protein,
                    f.carbs, f.fiber, f.portion, f.date
                ])

    def load_food(self, filename):
        if not os.path.exists(filename):
            return []

        food_log = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                food_log.append(FoodEntry(
                    row["Name"],
                    float(row["Calories"]),
                    float(row["Protein"]),
                    float(row["Carbs"]),
                    float(row["Fiber"]),
                    float(row["Portion"]),
                    datetime.fromisoformat(row["Date"]).date()
                ))

        return food_log

    # ========= WEIGHT =========
    def save_weight(self, weight_log, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Weight", "Date"])

            for w in weight_log:
                writer.writerow([w.weight, w.date])

    def load_weight(self, filename):
        if not os.path.exists(filename):
            return []

        weight_log = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                weight_log.append(WeightEntry(
                    float(row["Weight"]),
                    datetime.fromisoformat(row["Date"]).date()
                ))

        return weight_log

    # ========= USER =========
    def save_user(self, user, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Weight", "Calories", "Protein", "Carbs", "Fiber"])
            writer.writerow([
                user.get_name(),
                user.get_weight(),
                user.get_goal(),
                user.get_macro_goals()["protein"],
                user.get_macro_goals()["carbs"],
                user.get_macro_goals()["fiber"]
            ])

    def load_user(self, filename):
        if not os.path.exists(filename):
            return None

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                return User(
                    row["Name"],
                    float(row["Weight"]),
                    int(row["Calories"]),
                    int(row["Protein"]),
                    int(row["Carbs"]),
                    int(row["Fiber"])
                )