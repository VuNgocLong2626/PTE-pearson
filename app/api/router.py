from fastapi import APIRouter

from app.api.routers import basic as api_basic


router = APIRouter()


router.include_router(api_basic.router)
