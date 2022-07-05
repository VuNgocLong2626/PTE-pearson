from pydantic import (
    BaseModel,
    Field,
    EmailStr
)
from datetime import date


class UserUsername(BaseModel):
    username: str = Field(
        min_length=2, max_length=20,
        alias='username'
    )


class UserPassWord(BaseModel):
    password: str = Field(
        min_length=8, max_length=20,
        alias='password'
    )


class DayOfBirth(BaseModel):
    dob: date = Field(None, alias='dob')


class FirstName(BaseModel):
    first_name: str = Field(
        min_length=2,
        alias='first_name'
    )


class LastName(BaseModel):
    last_name: str = Field(
        min_length=2,
        alias='last_name'
    )


class Email(BaseModel):
    email: EmailStr = Field(alias='email')
