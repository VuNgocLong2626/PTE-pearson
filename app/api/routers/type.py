from fastapi import APIRouter

from app.models.schemas import type as _type_schemas
from app.services.type import TypeService
from typing import List


router = APIRouter()
type_service = TypeService()


@router.post(
    "/create-type"
)
async def create_type(type_in: _type_schemas.TypeCreate):
    response = type_service.create_type(type_in)
    return response


@router.get(
    "/get-all-info-type",
    response_model=List[_type_schemas.TypeDeatil]
)
async def get_all_info_type():
    response = type_service.get_all_info()
    return response


@router.get(
    "/get-info-type-by-id",
    response_model=_type_schemas.TypeDeatil
)
async def get_info_type_by_id(id_info: str):
    response = type_service.get_info_type_by_id(id_info)
    return response


@router.put(
    "/update-info-type"
)
async def update_info_type(type_in: _type_schemas.TypeDeatil):
    response = type_service.update_type(type_in)
    return response
