from pydantic import BaseModel, Field
from typing import Annotated

class Product(BaseModel):
    price: Annotated[float, Field(gt=0)]
    discount_percent: Annotated[int, Field(ge=0, le=100)]
    stock: Annotated[int, Field(ge=0, default=0)]
