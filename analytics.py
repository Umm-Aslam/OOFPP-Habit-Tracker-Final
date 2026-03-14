
from typing import List, Optional
from habit import Habit

"""
Analytics Module for the Reflection & Archiving Habit Tracker.
Uses Functional Programming (FP) principles (filter, map, pure functions).
"""

def get_active_habits(habits: List[Habit]) -> List[Habit]:
    """Uses filter to return habits that are currently being tracked (not archived)."""
    return list(filter(lambda h: not h.is_archived, habits))

def get_all_habit_names(habits: List[Habit]) -> List[str]:
    """Uses map to extract only the names of all habits."""
    return list(map(lambda h: h.name, habits))

def get_habits_by_periodicity(habits: List[Habit], period: str) -> List[Habit]:
    """Filters habits based on their periodicity (daily/weekly)."""
    return list(filter(lambda h: h.periodicity.lower() == period.lower(), habits))

def get_longest_streak_all(habits: List[Habit]) -> int:
    """Calculates max streak active across all tracked habits using map."""
    active = get_active_habits(habits)
    if not active:
        return 0
    return max(map(lambda h: h.get_streak(), active))

def calculate_total_consistency_score(habits: List[Habit]) -> float:
    """Calculates the average streak across all active habits."""
    active = get_active_habits(habits)
    if not active:
        return 0.0
    total_streaks = sum(map(lambda h: h.get_streak(), active))
    return round(total_streaks / len(active), 2)

def get_all_reflections(habits: List[Habit]) -> List[str]:
    """Aggregates all user reflections/notes into a single list."""
    notes = []
    for h in habits:
        notes.extend(h.reflections.values())
    return notes

def find_habit(habits: List[Habit], name: str) -> Optional[Habit]:
    """Utility to find a habit object by its name."""
    return next((h for h in habits if h.name.lower() == name.lower()), None)