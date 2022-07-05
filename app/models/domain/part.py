from pydantic import BaseModel, Field


class NamePart(BaseModel):
    name_part: str = Field(
        min_length=2, max_length=20,
        alias='name_part'
    )


class Title(BaseModel):
    title: str = Field(..., alias="title")


class Time(BaseModel):
    time: str = Field(..., alias='time')


class Scores(BaseModel):
    scores: int = Field(..., alias='scores')


class QuantityQuestion(BaseModel):
    quantity_question: int = Field(..., alias='quantity_question')


class NumberOfCorrectAnswer(BaseModel):
    number_of_correct_answer: int = Field(alias='number_of_correct_answer')
