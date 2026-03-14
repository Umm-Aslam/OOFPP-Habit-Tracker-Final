
import unittest
from datetime import datetime, timedelta
from habit import Habit
import analytics

class TestReflectionTracker(unittest.TestCase):
    def setUp(self):
        self.daily_habit = Habit("Testing Daily", "daily")
        self.habits_list = [self.daily_habit]

    def test_habit_initialization(self):
        self.assertEqual(self.daily_habit.name, "Testing Daily")
        self.assertFalse(self.daily_habit.is_archived)

    def test_reflection_logging(self):
        self.daily_habit.add_completion(reflection="Great day")
        self.assertEqual(len(self.daily_habit.reflections), 1)
        self.assertIn("Great day", self.daily_habit.reflections.values())

    def test_streak_logic_daily(self):
        now = datetime.now()
        self.daily_habit.add_completion(now.isoformat())
        self.daily_habit.add_completion((now - timedelta(days=1)).isoformat())
        self.assertEqual(self.daily_habit.get_streak(), 2)

    def test_streak_reset_on_miss(self):
        three_days_ago = (datetime.now() - timedelta(days=3)).isoformat()
        self.daily_habit.add_completion(three_days_ago)
        self.assertEqual(self.daily_habit.get_streak(), 0)

    def test_archiving_logic(self):
        self.daily_habit.toggle_archive()
        self.assertTrue(self.daily_habit.is_archived)
        active = analytics.get_active_habits(self.habits_list)
        self.assertNotIn(self.daily_habit, active)

    def test_consistency_score_analytics(self):
        now = datetime.now()
        self.daily_habit.add_completion(now.isoformat())
        score = analytics.calculate_total_consistency_score(self.habits_list)
        self.assertEqual(score, 1.0)

if __name__ == "__main__":
    unittest.main()