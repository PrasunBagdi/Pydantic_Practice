from pydantic import BaseModel, Field
from typing import Annotated
from decimal import Decimal

class Price(BaseModel):
    amount: Annotated[Decimal, Field(max_digits=10, decimal_places=2)]