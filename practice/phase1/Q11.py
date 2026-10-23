from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4
from datetime import datetime, date
from decimal import Decimal

class Transaction(BaseModel):
    id: Annotated[UUID, Field(default_factory=uuid4)]
    amount: Decimal
    created_at: Annotated[datetime, Field(default_factory=datetime.now)]
    due_date: date