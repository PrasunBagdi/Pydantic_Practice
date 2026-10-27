from pydantic import BaseModel, model_validator
from typing import Literal

class Shipping(BaseModel):
    method: Literal["pickup", "delivery"]
    address: str = None
    store_id: str = None

    @model_validator(mode="after")
    def check_method(self):
        if (self.method == "pickup") and (not self.store_id):
            raise ValueError("store_id is required for pickup")
        if (self.method == "delivery") and (not self.address):
            raise ValueError("address is required for delivery")
        return self

print(Shipping(method="delivery", address="1 Main St"))
print(Shipping(method="pickup", store_id="S1"))
print(Shipping(method="pickup"))