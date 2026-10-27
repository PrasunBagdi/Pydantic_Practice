from pydantic import BaseModel, model_validator

class Signup(BaseModel):
    username: str
    password: str

    @model_validator(mode="before")
    @classmethod
    def normalize_keys(cls, data):
        if isinstance(data, dict):
            if "user" in data and not "username" in data:
                data["username"] = data.pop("user")
            if "pwd" in data and not "password" in data:
                data["password"] = data.pop("pwd")
            return data

print(Signup(user="prasun", pwd="awdada"))