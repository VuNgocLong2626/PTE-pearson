from datetime import time
from typing import List
from fastapi import APIRouter, UploadFile, File, Form

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
    time: time = Form(..., alias='Time'),
    id_type: str = Form(..., alias='IdType'),
    name_type: str = Form(..., alias='TypeName')
):
    question_in = _question_schemas.QuestionCreate(**{
        'Title': title,
        'Content': content,
        'Time': str(time),
        'IdType': id_type,
        'NameType': name_type
    })
    response = question_service.create_question(question_in, file)
    return response


@router.get(
    "/get-info-question-by-id",
    response_model=_question_schemas.QuestionDetail
)
async def get_info_question_by_id(id_question: str):
    response = question_service.get_info_question_by_id(id_question)
    return response


@router.get(
    "/search-question-by-type",
    response_model=List[_question_schemas.QuestionDetail]
)
async def get_search_question_by_type(id_type: str):
    response = question_service.search_question_by_id_type(id_type)
    return response


@router.put(
    "/update-question-info"
)
async def update_question_info(
    file: UploadFile = File(..., alias='File'),
    id_question: str = Form(..., alias='IdQuestion'),
    title: str = Form(..., alias='Title'),
    content: str = Form(..., alias='Content'),
    time: time = Form(..., alias='Time'),
    id_type: str = Form(..., alias='IdType'),
    name_type: str = Form(..., alias='TypeName')
):
    question_in = _question_schemas.QuestionUpdate(**{
        'IdQuestion': id_question,
        'Title': title,
        'Content': content,
        'Time': str(time),
        'IdType': id_type,
        'NameType': name_type
    })
    response = question_service.update_question(question_in, file)
    return response


@router.delete(
    "/delete-question"
)
async def delete_question(
    id_question: str
):
    response = question_service.delete_question(id_question)
    return response


@router.get(
    "/get-all-question",
    response_model=List[_question_schemas.QuestionDetail]
)
async def get_all_question():
    resopnse = question_service.get_all_question()
    return resopnse
