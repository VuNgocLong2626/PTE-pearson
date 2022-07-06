from fastapi import APIRouter

from app.api.routers import (
    basic as api_basic,
    part as api_part
)


router = APIRouter()


router.include_router(api_basic.router)
router.include_router(api_part.router)
