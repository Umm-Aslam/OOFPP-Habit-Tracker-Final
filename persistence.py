
import json
import os
from datetime import datetime, timedelta
from habit import Habit

DATA_FILE = "habit_data.json"

def save_all(habits):
    """Saves the entire list of habit objects to JSON."""
    with open(DATA_FILE, 'w') as f:
        json.dump([h.to_dict() for h in habits], f, indent=4)

def load_all():
    """Loads habits from JSON or initializes with 4-week test data if file is missing."""
    if not os.path.exists(DATA_FILE):
        return initialize_test_data()

    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Habit.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError):
        return initialize_test_data()

def initialize_test_data():
    """
    Seeds the system with 5 habits and 4 weeks of historical data.
    This satisfies the professor's requirement for 'time-series data'.
    """
    habits = []
    now = datetime.now()

    # 1. Meditate (Daily) - Perfect 28-day streak
    h1 = Habit("Daily Meditation", "daily")
    for i in range(28):
        h1.add_completion((now - timedelta(days=i)).isoformat(), "Felt very calm today.")
    habits.append(h1)

    # 2. Gym (Weekly) - 4-week consistency
    h2 = Habit("Weightlifting", "weekly")
    for i in range(4):
        h2.add_completion((now - timedelta(weeks=i)).isoformat(), f"Week {4-i} workout done.")
    habits.append(h2)

    # 3. Reading (Daily) - Broken streak (missed the last 3 days)
    h3 = Habit("Read 10 Pages", "daily")
    for i in range(3, 28): # Skip days 0, 1, 2
        h3.add_completion((now - timedelta(days=i)).isoformat())
    habits.append(h3)

    # 4. Coding (Daily) - New habit, 5-day streak
    h4 = Habit("Learn Python", "daily")
    for i in range(5):
        h4.add_completion((now - timedelta(days=i)).isoformat(), "Studied OOP concepts.")
    habits.append(h4)

    # 5. Morning Run (Daily) - Archived habit (Preserved history)
    h5 = Habit("Morning Run", "daily", is_archived=True)
    for i in range(30, 40): # Completed 10 days, a month ago
        h5.add_completion((now - timedelta(days=i)).isoformat())
    habits.append(h5)

    save_all(habits)
    return habits