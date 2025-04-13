from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        from_attributes = True


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class UpdateUser(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None


if __name__ == '__main__':
    user = RegisterUser(name='Jezreel', email='mastering', password='Hello')
    print(user.model_dump())
    print(user.model_dump_json())
