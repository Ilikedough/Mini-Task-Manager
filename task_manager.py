from dataclasses import (dataclass,field)
from enum import Enum
import uuid
import datetime
import logger

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
    due_date: datetime.datetime = field(default_factory=datetime.datetime.today)
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __str__(self) -> str:
        return (f"Task: \n"
                f"Id: {self.id}\n"
                f"Name: {self.name}\n"
                f"Owner: {self.owner}\n"
                f"Progress: {self.progress.value}\n"
                f"Priority: {self.priority.value}\n"
                f"Due Date: {self.due_date}"
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

        priority = {Priority.LOW:1,Priority.MEDIUM:2,Priority.HIGH:3}

        return (priority[self.priority],self.due_date) > (priority[other.priority],other.due_date)

class TaskManager():
    def __init__(self) -> None:
        self.tasks = []
        self.logger = logger.setup_logger("TMlog","TM.log")
    
    def add(self,task) -> bool:
        if isinstance(task,Task):
            if task in self.tasks:
                self.logger.warning(f"Attempted adding duplicate task with id: {task.id}")
                return False
            self.tasks.append(task)
            self.logger.info(f"Task added successfully (id={task.id}, name='{task.name}')")
            return True
        self.logger.warning(f"Task is of invalid type {type(task).__name__}")
        return False
    
    def delete(self,task) -> bool:
        if isinstance(task,Task):
            if task in self.tasks:
                self.tasks.remove(task)
                self.logger.info(f"Task deleted successfully (id={task.id}, name='{task.name}')")
                return True
            self.logger.warning(f"Task with id: {task.id} is not in the tasks")
            return False
        self.logger.warning(f"Task is of invalid type {type(task).__name__}")
        return False

    def edit(self,task,info) -> bool:
        if not isinstance(task,Task):
            self.logger.warning(f"Task is of invalid type {type(task).__name__}")
            return False
        
        if not info:
            self.logger.info(f"No changes requested for task {task.id}")
        
        if "progress" in info and not isinstance(info["progress"], Progress):
            self.logger.warning(f"{type(info['progress']).__name__} is an invalid type for progress")
            return False

        if "priority" in info and not isinstance(info["priority"], Priority):
            self.logger.warning(f"{type(info['priority']).__name__} is an invalid type for priority")
            return False
        
        if "due_date" in info and not isinstance(info["due_date"], datetime.datetime):
            self.logger.warning(f"{type(info['due_date']).__name__} is an invalid type for due_date")
            return False
        
        if task not in self.tasks:
            self.logger.warning(f"Attempted to edit unmanaged task (id={task.id})")
            return False

        
        
        properties = ("name","description","owner","progress","priority","due_date")

        invalid = set(info) - set(properties)

        if invalid:
            self.logger.warning(f"Ignoring unknown fields: {invalid}")
            
        for prop in properties:  
            if prop in info:
                setattr(task,prop,info[prop])
        self.logger.info(f"Task updated successfully (id={task.id}, fields={list(info.keys())})")
        return True
    
    def search(self,id):
        for task in self.tasks:
            if task.id == id:
                self.logger.info(f"Task found (id={id})")
                return task
        self.logger.warning(f"Id: {id} was not found")
        return None
    
    def filter(self,info):
        if not info:
            self.logger.info("Empty filter supplied; returning all tasks")
        properties = ("name","description","owner","progress","priority","due_date")
        invalid = set(info) - set(properties)

        if invalid:
            self.logger.warning(f"Ignoring unknown filter fields: {invalid}")
        result = []

        for task in self.tasks:
            match = True
            for prop in properties:
                if prop in info:
                    if getattr(task, prop) != info[prop]:
                        match = False
                        break
        
                        
            if match:
                result.append(task)
        self.logger.info(f"Filter completed successfully. {len(result)} task(s) matched.")
        return result