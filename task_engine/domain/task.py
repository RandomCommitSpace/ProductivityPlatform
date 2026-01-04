from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Task:
    id: int
    title: str
    priority: Priority
    estimated_minutes: int
    deadline: datetime
