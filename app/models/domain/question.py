from pydantic import BaseModel, Field


class Title(BaseModel):
    title: str = Field(..., alias="title")


class Content(BaseModel):
    content: int = Field(..., alias='content')


class Scores(BaseModel):
    scores: int = Field(..., alias='scores')


class Answer(BaseModel):
    answer: dict = Field(..., alias='Answer')


class Solution(BaseModel):
    solution: dict = Field(..., alias='Solution')
