from pydantic import BaseModel, Field
from datetime import time as _time


class PartName(BaseModel):
    part_name: str = Field(
        min_length=2, max_length=20,
        alias='PartName'
    )


class Title(BaseModel):
    title: str = Field(..., alias="Title")


class Time(BaseModel):
    time: _time = Field(
        ...,
        example="00:12:00",
        alias='Time'
    )


class Scores(BaseModel):
    scores: int = Field(..., alias='Scores')


class QuestionQuantity(BaseModel):
    question_quantity: int = Field(..., alias='QuestionQuantity')


class NumberOfCorrectAnswer(BaseModel):
    number_of_correct_answer: int = Field(alias='NumberOfCorrectAnswer')
