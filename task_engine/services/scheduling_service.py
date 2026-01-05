from typing import List
from task_engine.domain.task import Task
from task_engine.domain.schedule import Schedule
from core.contracts.scheduler import SchedulerStrategy


class SchedulingService:
    """Application service to generate schedules using a strategy."""

    def __init__(self, strategy: SchedulerStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SchedulerStrategy) -> None:
        """Switch scheduling strategy at runtime."""
        self._strategy = strategy

    def generate_schedule(self, tasks: List[Task]) -> Schedule:
        return self._strategy.generate_schedule(tasks)
