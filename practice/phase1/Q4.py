from pydantic import BaseModel, Field
from typing import Annotated

class Item(BaseModel):
    name: str
    price: float

class Inventory(BaseModel):
    items: Annotated[list[Item], Field(default_factory=list)]
    by_warehouse: Annotated[dict[str, Item], Field(default_factory=dict)]

item1 = Item(name="PlayStation", price=69000)
item2 = Item(name="XBox", price=67000)
inv = Inventory(
    items = [item1, item2],
    by_warehouse = {"east":item1, "north":item2}
)

print(inv)