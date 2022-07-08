from fastapi import APIRouter

from app.api.routers import (
    basic as api_basic,
    user as api_user
)


router = APIRouter()


router.include_router(
    api_basic.router,
    prefix="/basic",
    tags=["Basic"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_user.router,
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)
