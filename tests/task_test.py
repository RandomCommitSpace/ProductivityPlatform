from datetime import datetime, timedelta
from task_engine.domain.task import Task, Priority
from task_engine.services.scheduling_service import SchedulingService
from task_engine.algorithms.fifo_scheduler import FIFOScheduler
from task_engine.algorithms.priority_scheduler import PriorityScheduler

tasks = [
    Task(1, "Task 1", Priority.MEDIUM, 60, datetime.now() + timedelta(hours=2)),
    Task(2, "Task 2", Priority.HIGH, 30, datetime.now() + timedelta(hours=1)),
    Task(3, "Task 3", Priority.LOW, 45, datetime.now() + timedelta(hours=3)),
]

service = SchedulingService(FIFOScheduler())
schedule = service.generate_schedule(tasks)
print("FIFO:", [t.title for t in schedule.tasks])

service.set_strategy(PriorityScheduler())
schedule = service.generate_schedule(tasks)
print("Priority:", [t.title for t in schedule.tasks])



# python -m tests.task_test
