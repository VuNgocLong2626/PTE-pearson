from pydantic import BaseModel, Field


class Title(BaseModel):
    title: str = Field(..., alias="Title")


class Content(BaseModel):
    content: str = Field(..., alias='Content')


class Scores(BaseModel):
    scores: int = Field(..., alias='Scores')


class Answer(BaseModel):
    answer: dict = Field(..., alias='Answer')


class Solution(BaseModel):
    solution: dict = Field(..., alias='Solution')


class Path(BaseModel):
    path: str = Field(None, alias='Path')


class SolutionFile(BaseModel):
    solution_file: str = Field(..., alias='SolutionFile')


class Time(BaseModel):
    time: str = Field(..., example="00:12:00", alias="Time")
