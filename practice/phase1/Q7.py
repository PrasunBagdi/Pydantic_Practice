from pydantic import BaseModel, Field
from typing import Annotated

class Account(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=20)]
    password: Annotated[str, Field(min_length=8)]
    zipcode: Annotated[str, Field(pattern=r"^\d{5}$")]
