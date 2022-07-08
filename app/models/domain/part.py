from pydantic import BaseModel, Field
from datetime import time as _time


class PartName(BaseModel):
    part_name: str = Field(
        min_length=2, max_length=20,
        alias='NamePart'
    )


class Title(BaseModel):
    title: str = Field(..., alias="Title")


class Time(BaseModel):
    time: str = Field(..., alias='Time')


class Scores(BaseModel):
    scores: int = Field(..., alias='Scores')


class QuantityQuestion(BaseModel):
    quantity_question: int = Field(..., alias='QuantityQuestion')


class NumberOfCorrectAnswer(BaseModel):
    number_of_correct_answer: int = Field(alias='NumberOfCorrectAnswer')
