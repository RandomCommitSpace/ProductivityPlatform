from dataclasses import dataclass
from typing import List
from datetime import datetime
from task_engine.domain.task import Task


@dataclass
class Schedule:
    generated_at: datetime
    tasks: List[Task]
