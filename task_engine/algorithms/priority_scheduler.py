from datetime import datetime
from typing import List
from core.contracts.scheduler import SchedulerStrategy
from task_engine.domain.task import Task, Priority
from task_engine.domain.schedule import Schedule


class PriorityScheduler(SchedulerStrategy):
    """Schedules tasks based on their priority."""

    def generate_schedule(self, tasks: List[Task]) -> Schedule:
        sorted_tasks = sorted(tasks, key=lambda t: t.priority.value, reverse=True)
        return Schedule(generated_at=datetime.now(), tasks=sorted_tasks)
