from datetime import date, timedelta
from habit_engine.domain.habit import Habit

class HabitAnalyticsService:
    """Provides analytical insights about habits."""

    def calculate_consistency(self, habit: Habit) -> float:
        if not habit.completions:
            return 0.0
        total_days = (date.today() - habit.start_date).days + 1
        return len(set(habit.completions)) / max(total_days, 1)

    def current_streak(self, habit: Habit) -> int:
        if not habit.completions:
            return 0
        streak = 0
        day = date.today()
        completion_set = set(habit.completions)
        while day in completion_set:
            streak += 1
            day -= timedelta(days=1)
        return streak
