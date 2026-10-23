from pydantic import BaseModel, Field
from typing import Annotated

class Product(BaseModel):
    name: Annotated[str, Field(name="Product Name", description="Display name shown to customers")]
    price: Annotated[float, Field(gt=0, name="Product Price", description="Unit price in USD, must be positive")]
