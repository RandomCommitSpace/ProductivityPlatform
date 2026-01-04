from dataclasses import dataclass, field
from typing import List
from datetime import date


@dataclass
class Habit:
    id: int
    name: str
    frequency_per_week: int
    start_date: date
    completions: List[date] = field(default_factory=list)

    def record_completion(self, completion_date: date) -> None:
        if completion_date < self.start_date:
            raise ValueError("Completion date cannot be before habit start date.")
        self.completions.append(completion_date)
