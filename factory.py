from trackers import FoodTracker, WeightTracker


class TrackerFactory:
    _trackers = {
        "food": FoodTracker,
        "weight": WeightTracker
    }

    @classmethod
    def create_tracker(cls, tracker_type):
        if tracker_type in cls._trackers:
            return cls._trackers[tracker_type]()
        raise ValueError("Invalid tracker type")