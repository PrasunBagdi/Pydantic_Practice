from pydantic import BaseModel, EmailStr, model_validator

class UserFilter(BaseModel):
    user_id: int = None
    email: EmailStr = None

    @model_validator(mode="after")
    def only_one_parameter(self):
        if self.user_id and self.email:
            raise ValueError("only one parameter must be set")
        return self

print(UserFilter(user_id="25"))
print(UserFilter(email="a@b.com"))
uf3 = UserFilter(user_id="80", email="c@d.com")