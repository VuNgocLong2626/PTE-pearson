from pydantic import (
    BaseModel,
    Field,
    EmailStr
)
from datetime import date


class UserUsername(BaseModel):
    username: str = Field(
        min_length=2, max_length=20,
        alias='Username'
    )


class UserPassWord(BaseModel):
    password: str = Field(
        min_length=8, max_length=20,
        alias='Password'
    )


class DayOfBirth(BaseModel):
    dob: date = Field(None, alias='DayOfBirth')


class FirstName(BaseModel):
    first_name: str = Field(
        min_length=2,
        alias='FirstName'
    )


class LastName(BaseModel):
    last_name: str = Field(
        min_length=2,
        alias='LastName'
    )


class Email(BaseModel):
    email: EmailStr = Field(alias='Email')
