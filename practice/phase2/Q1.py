from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username", mode="after")
    @classmethod
    def alnum_check_on_username(cls, v:str):
        if not v.isalnum():
            raise ValueError("username must be alphanumeric")
        return v

u1 = User(username="prasun458")
print(u1)
u2 = User(username="adw2568*/.")
