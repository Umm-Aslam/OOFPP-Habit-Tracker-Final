from datetime import datetime, timedelta

class Habit:
    """
    Object-Oriented model representing a habit.
    Handles the state of the habit, including completion history,
    qualitative reflections, and archiving logic.
    """
    def __init__(self, name, periodicity, created_at=None, completions=None, reflections=None, is_archived=False):
        self.name = name
        self.periodicity = periodicity  # Expected: 'daily' or 'weekly'
        self.created_at = created_at if created_at else datetime.now().isoformat()
        self.completions = completions if completions else []
        # Reflections are stored as a dictionary mapping completion timestamps to user notes
        self.reflections = reflections if reflections else {}
        self.is_archived = is_archived

    def add_completion(self, timestamp=None, reflection=""):
        """Logs a completion event with an optional reflection."""
        if not timestamp:
            timestamp = datetime.now().isoformat()
        self.completions.append(timestamp)
        if reflection:
            self.reflections[timestamp] = reflection

    def toggle_archive(self):
        """Logically archives or unarchives the habit."""
        self.is_archived = not self.is_archived

    def get_streak(self):
        """
        Calculates the current streak of the habit.
        Respects periodicity (daily vs weekly) and resets if a period is missed.
        """
        if not self.completions or self.is_archived:
            return 0

        # Sort completions in descending order to check from most recent backwards
        dates = sorted([datetime.fromisoformat(d).date() for d in self.completions], reverse=True)
        # Remove duplicates from the same day
        unique_dates = sorted(list(set(dates)), reverse=True)

        streak = 0
        current_date = datetime.now().date()

        # Determine the 'grace period' based on periodicity
        delta_limit = 1 if self.periodicity == 'daily' else 7

        # If the most recent completion is older than the periodicity, streak is 0
        if (current_date - unique_dates[0]).days > delta_limit:
            return 0

        # Iterate backwards through completion dates
        last_date = unique_dates[0]
        for d in unique_dates:
            if (last_date - d).days <= delta_limit:
                streak += 1
                last_date = d
            else:
                break
        return streak

    def to_dict(self):
        """Serializes habit data for JSON storage."""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "completions": self.completions,
            "reflections": self.reflections,
            "is_archived": self.is_archived
        }

    @classmethod
    def from_dict(cls, data):
        """Reconstructs a Habit object from dictionary data."""
        return cls(
            name=data['name'],
            periodicity=data['periodicity'],
            created_at=data['created_at'],
            completions=data['completions'],
            reflections=data['reflections'],
            is_archived=data.get('is_archived', False)
        )