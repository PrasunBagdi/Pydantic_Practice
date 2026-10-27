from pydantic import BaseModel, field_validator

class Product(BaseModel):
    price: float

    @field_validator("price", mode="before")
    @classmethod
    def correct_price_format(cls, v):
        if isinstance(v, str):
            v = v.replace("$", "").replace(",", "")
        return v

p1 = Product(price=69)
print(p1.price)
p2 = Product(price="$67,000")
print(p2.price)