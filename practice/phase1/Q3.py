from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Customer(BaseModel):
    name: str
    address: Address

c1 = Customer(name="Prasun", address={"street":"somewhere", "city":"somecity", "zip_code":"dawdfwfwa"})
print(c1)
print(c1.address)
