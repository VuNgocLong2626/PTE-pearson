from fastapi import APIRouter
from app.models.schemas import user as _user_domain
from app.services.user import UserService


router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/create",
    response_model=_user_domain.UserDetail
)
async def create_user(user_in: _user_domain.UserCreate):
    respon = UserService.create_user(user_in)
    return respon


@router.get(
    "/get-info",
    response_model_by_alias=True,
    response_model=_user_domain.UserDetail
)
async def get_info_user(username: str):
    respon = UserService.get_info_user(username)
    return respon


@router.delete(
    "/delete-user"
)
async def delete_user(username: str):
    respon = UserService.delete_user_by_username(username)
    return respon


@router.put(
    "/update-info"
)
async def update_info_user(user_in: _user_domain.UserUpdateInfo):
    respon = UserService.update_user_info(user_in)
    return respon
