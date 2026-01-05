# Enable multiple scheduling algorithms
# Enforce Strategy Pattern

from abc import ABC, abstractmethod
from typing import List
from task_engine.domain.task import Task
from task_engine.domain.schedule import Schedule

class SchedulerStrategy(ABC):
    """Strategy interface for task scheduling algorithms."""

    @abstractmethod
    def generate_schedule(self, tasks: List[Task]) -> Schedule:
        pass
