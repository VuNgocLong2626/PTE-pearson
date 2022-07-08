from pydantic import BaseModel, Field


class NameTest(BaseModel):
    name_test: str = Field(..., alias='NameTest')


class Title(BaseModel):
    title: str = Field(..., alias="Title")


class Time(BaseModel):
    time: str = Field(..., alias='Time')


class Scores(BaseModel):
    scores: int = Field(..., alias='Scores')


class QuantityQuestion(BaseModel):
    quantity_question: int = Field(..., alias='QuantityQuestion')
