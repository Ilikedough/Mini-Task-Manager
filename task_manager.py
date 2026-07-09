from dataclasses import (dataclass,field)
import uuid

@dataclass(kw_only=True)
class Task():
    name: str
    description: str
    owner: str
    progress: str = "TODO"
    priority: str = "Low"
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    

