from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    quantity: int = 0
    in_stock: bool = True

p1 = Product(
    name = "pen",
    price = "10",
    quantity = 5.0
)
print(p1)