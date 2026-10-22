from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Annotated
from datetime import datetime

class Task(BaseModel):
    title: str
    id: Annotated[UUID, Field(default_factory=uuid4)]
    tags: Annotated[list[str], Field(default_factory=list)]
    created_at: Annotated[datetime, Field(default_factory=datetime.now)]

task1 = Task(title="code")
print(task1)