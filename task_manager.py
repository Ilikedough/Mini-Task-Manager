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

    def __str__(self) -> str:
        return (f"Task: \n"
                f"Id: {self.id}\n"
                f"Name: {self.name}\n"
                f"Owner: {self.owner}\n"
                f"Progress: {self.progress.value}\n"
                f"Priority: {self.priority.value}"
                )

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Task):
            return False
        attributes = ("name", "description", "owner", "progress", "priority", "id")

        for attr in attributes:
            if getattr(self,attr) != getattr(value,attr):
                return False
        return True
    
    def __lt__(self, other):
        if not isinstance(other, Task):
            return NotImplemented

        values = {Priority.LOW:1,Priority.MEDIUM:2,Priority.HIGH:3}

        return values[self.priority] > values[other.priority]
    

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
        
        if "progress" in info and not isinstance(info["progress"], Progress):
            return False

        if "priority" in info and not isinstance(info["priority"], Priority):
            return False
        
        properties = ("name","description","owner","progress","priority")
        for prop in properties:  
            if prop in info:
                setattr(task,prop,info[prop])
        return True
    
    def search(self,id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None
    
    def filter(self,info):
        properties = ("name","description","owner","progress","priority")
        result = []

        for task in self.tasks:
            match = True
            for prop in properties:
                if prop in info:
                    if getattr(self,prop) != task[prop]:
                        match = False
                        break
        
                        
            if match:
                result.append(task)
        
        return result