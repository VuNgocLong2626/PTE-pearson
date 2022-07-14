from fastapi import APIRouter

from app.api.routers import (
    basic as api_basic,
    part as api_part,
    user as api_user,
    question as api_question,
    type as api_type,
    test as api_test,
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

router.include_router(
    api_part.router,
    prefix="/part",
    tags=["Part"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_question.router,
    prefix="/question",
    tags=["Question"],
    responses={404: {"description": "Not found"}}
)

router.include_router(
    api_type.router,
    prefix="/type",
    tags=["Type"],
    responses={404: {"description": "Not found"}}
)

router.include_router(
    api_test.router,
    prefix="/test",
    tags=["Test"],
    responses={404: {"description": "Not found"}}
)