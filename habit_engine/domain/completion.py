from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class HabitCompletion:
    habit_id: int
    completed_on: date
