from pydantic import BaseModel, field_validator

class Profile(BaseModel):
    first_name: str
    last_name: str
    bio: str = ""

    @field_validator("*")
    @classmethod
    def remove_whitespace(cls, v:str):
        return v.strip()

    @field_validator("first_name", "last_name")
    @classmethod
    def reject_blank(cls, v:str):
        if not v.strip():
            raise ValueError("Names cannot be blank")
        return v

person1 = Profile(first_name=" Prasun ", last_name="Bagdi")
print(person1)
person2 = Profile(first_name="", last_name="", bio="adwwa")