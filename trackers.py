from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Tracker(ABC):
    @abstractmethod
    def add_entry(self, data):
        pass


class FoodTracker(Tracker):
    def __init__(self):
        self.food_log = []

    def add_entry(self, food):
        self.food_log.append(food)

    def get_today_entries(self):
        today = datetime.now().date()
        return [f for f in self.food_log if f.date == today]

    def get_today_calories(self):
        return sum(f.calories for f in self.get_today_entries())

    def get_today_protein(self):
        return sum(f.protein for f in self.get_today_entries())

    def get_today_carbs(self):   
        return sum(f.carbs for f in self.get_today_entries())

    def get_today_fiber(self):  
        return sum(f.fiber for f in self.get_today_entries())

    def get_last_7_days_calories(self):
        today = datetime.now().date()
        return sum(
            f.calories for f in self.food_log
            if (today - f.date).days <= 7
        )


class WeightTracker(Tracker):
    def __init__(self):
        self.weight_log = []

    def add_entry(self, entry):
        self.weight_log.append(entry)

    def get_latest_weight(self):
        if not self.weight_log:
            return None
        return self.weight_log[-1].weight

    def get_weight_change(self):
        if len(self.weight_log) < 2:
            return 0
        return self.weight_log[-1].weight - self.weight_log[0].weight