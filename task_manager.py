from dataclasses import (dataclass,field)
from enum import Enum
import uuid


class Progress(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass(kw_only=True)
class Task():
    name: str
    description: str
    owner: str
    progress: Progress = Progress.TODO
    priority: Priority = Priority.LOW
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    

