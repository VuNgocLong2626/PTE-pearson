from pydantic import BaseModel, Field


class NameTest(BaseModel):
    name_test: str = Field(..., alias='NameTest')


class Title(BaseModel):
    title: str = Field(..., alias="Title")


class Time(BaseModel):
    time: str = Field(
        ...,
        example='01:30:30',
        alias='Time'
    )


class Scores(BaseModel):
    scores: int = Field(None, alias='Scores')


class QuantityQuestion(BaseModel):
    quantity_question: int = Field(..., alias='QuantityQuestion')
