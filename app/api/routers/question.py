from typing import List
from fastapi import APIRouter, UploadFile, File, Form
from pydantic import Field
from datetime import time

from app.services.question import QuestionService
from app.models.schemas import question as _question_schemas


router = APIRouter()
question_service = QuestionService()


@router.post(
    "/create-question"
)
async def create_question(
    file: UploadFile = File(..., alias='File'),
    title: str = Form(..., alias='Title'),
    content: str = Form(..., alias='Content'),
    time: time = Form(..., alias='Time')
):
    question_in = _question_schemas.QuestionCreate(**{
        'Title': title,
        'Content': content,
        'Time': str(time)
    })
    resopnse = question_service.create_question(question_in, file)
    return resopnse


@router.get(
    "/get-file"
)
async def get_file():
    response = question_service.get_file()
    return response


@router.delete(
    "/delete-file"
)
async def delete_file():
    response = question_service.detete_file()
    return response
