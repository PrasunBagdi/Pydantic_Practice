from pydantic import BaseModel, Field
from typing import Annotated

class ApiUser(BaseModel):
    first_name: Annotated[str, Field(alias="firstName")]
    last_name: Annotated[str, Field(alias="lastName")]
    is_active: Annotated[bool, Field(alias="isActive")]
