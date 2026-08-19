from pydantic import BaseModel, EmailStr


class RegisterModel(BaseModel):
    email: EmailStr
    password: str
    name: str


class LoginModel(BaseModel):
    email: EmailStr
    password: str