from pydantic import BaseModel, EmailStr, HttpUrl

class Contact(BaseModel):
    email: EmailStr
    website: HttpUrl
