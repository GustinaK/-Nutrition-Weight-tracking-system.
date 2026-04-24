from datetime import datetime


class User:
    def __init__(self, name, weight, calorie_goal,
                 protein_goal, carbs_goal, fiber_goal):
        self._name = name
        self._weight = weight
        self._calorie_goal = calorie_goal
        self._protein_goal = protein_goal
        self._carbs_goal = carbs_goal
        self._fiber_goal = fiber_goal

    def update_weight(self, new_weight):
        if new_weight > 0:
            self._weight = new_weight

    def get_weight(self):
        return self._weight

    def get_name(self):
        return self._name

    def get_goal(self):
        return self._calorie_goal

    def get_macro_goals(self):
        return {
            "protein": self._protein_goal,
            "carbs": self._carbs_goal,
            "fiber": self._fiber_goal
        }


class FoodEntry:
    def __init__(self, name, calories, protein=0, carbs=0, fiber=0,
                 portion=1.0, date=None):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fiber = fiber
        self.portion = portion
        self.date = date or datetime.now().date()


class WeightEntry:
    def __init__(self, weight, date=None):
        self.weight = weight
        self.date = date or datetime.now().date()