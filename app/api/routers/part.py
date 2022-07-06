from fastapi import APIRouter

from app.services.part import PartService
from app.models.schemas import part as _part_schemas


router = APIRouter(
    prefix="/part",
    tags=["Part"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/create-part",
    response_model=_part_schemas.PartDetail
)
async def create_part(part_in: _part_schemas.PartCreat):
    respon = PartService.create_part(part_in)
    return respon
