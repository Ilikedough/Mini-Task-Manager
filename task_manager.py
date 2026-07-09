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
    

class TaskManager():
    def __init__(self) -> None:
        self.tasks = []
    
    def add(self,task) -> bool:
        if isinstance(task,Task):
            if task in self.tasks:
                return False
            self.tasks.append(task)
            return True
        return False
    
    def delete(self,task) -> bool:
        if isinstance(task,Task):
            if task in self.tasks:
                self.tasks.remove(task)
                return True
            return False
        return False

    def edit(self,task,info) -> bool:
        if not isinstance(task,Task):
            return False
        properties = ("name","description","owner","progress","priority")
        for prop in properties:  
            if prop in info:
                if prop in ("progress","priority"):
                    if not prop in (Progress, Priority):
                        return False
                setattr(task,prop,info[prop])
        return True
        