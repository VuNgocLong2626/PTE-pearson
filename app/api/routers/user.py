from fastapi import APIRouter
from app.models.schemas import user as _user_schemas
from app.services.user import UserService


router = APIRouter()
user_service = UserService()


@router.post(
    "/create-user",
    response_model=_user_schemas.UserDetail
)
async def create_user(user_in: _user_schemas.UserCreate):
    response = user_service.create_user(user_in)
    return response


@router.get(
    "/get-info-by-username",
    response_model_by_alias=True,
    response_model=_user_schemas.UserDetail
)
async def get_info_user(username: str):
    respon = user_service.get_info_user(username)
    return respon


@router.delete(
    "/delete-user-by-username"
)
async def delete_user(username: str):
    respon = user_service.delete_user_by_username(username)
    return respon


@router.put(
    "/update-info",
    response_model=_user_schemas.UserDetail
)
async def update_info_user(user_in: _user_schemas.UserUpdateInfo):
    respon = user_service.update_user_info(user_in)
    return respon
