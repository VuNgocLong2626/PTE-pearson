from fastapi import APIRouter

from app.api.routers import (
    basic as api_basic,
    user as api_user
)


router = APIRouter()


router.include_router(api_basic.router)
router.include_router(api_user.router)
