from pydantic import BaseModel, Field
from typing import Annotated, Literal

Username = Annotated[str, Field(min_length=3, max_length=20)]
Percentage = Annotated[int, Field(ge=0, le=100)]

class User(BaseModel):
    username: Username
    role: Literal["admin", "user", "guest"] = "user"

class Team(BaseModel):
    owner: Username
    progress: Percentage = 0