from typing import List
from fastapi import APIRouter

from app.services.part import PartService
from app.models.schemas import part as _part_schemas


router = APIRouter()
part_service = PartService()


@router.post(
    "/create-part",
    response_model=_part_schemas.PartDetail
)
async def create_part(part_in: _part_schemas.PartCreat):
    respon = part_service.create_part(part_in)
    return respon


@router.delete(
    "/delete-part-by-id"
)
async def delete_part_by_id(id_part: str):
    response = part_service.delete_part(id_part)
    return response


@router.get(
    "/get-info-by-id",
    response_model=_part_schemas.PartDetail
)
async def get_info_part_by_id(id_part: str):
    response = part_service.get_info_part(id_part)
    return response


@router.get(
    "/get-all-info",
    response_model=List[_part_schemas.PartDetail]
)
async def get_all():
    response = part_service.get_all_info_part()
    return response


@router.put(
    "/update-info-part"
)
async def update_info_part(part_in: _part_schemas.PartDetail):
    response = part_service.update_part(part_in)
    return response
