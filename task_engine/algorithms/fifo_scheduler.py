from datetime import datetime
from typing import List
from core.contracts.scheduler import SchedulerStrategy
from task_engine.domain.task import Task
from task_engine.domain.schedule import Schedule


class FIFOScheduler(SchedulerStrategy):
    """Schedules tasks in the order they are received."""

    def generate_schedule(self, tasks: List[Task]) -> Schedule:
        sorted_tasks = sorted(tasks, key=lambda t: t.id)  # FIFO by id
        return Schedule(generated_at=datetime.now(), tasks=sorted_tasks)
