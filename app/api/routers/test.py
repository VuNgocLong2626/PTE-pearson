from typing import List
from fastapi import APIRouter

from app.services.test import TestService
from app.models.schemas import test as _test_schemas


router = APIRouter()
test_service = TestService()


@router.post(
    "/create-test",
)
async def create_test(test_in: _test_schemas.TestCreate):
    response = test_service.create_test(test_in)
    return response


@router.get(
    "/get-all-test-info",
    response_model=List[_test_schemas.TestDetail]
)
async def get_all_test_info():
    response = test_service.get_all_info_test()
    return response


@router.get(
    "get-test-info-by-id",
    response_model=_test_schemas.TestDetail
)
async def get_test_info_by_id(id_test: str):
    response = test_service.get_test_info_by_id(id_test)
    return response


@router.put(
    "/update-test-info",

)
async def update_test_info(test_in: _test_schemas.TestDetail):
    response = test_service.update_test(test_in)
    return response


@router.get(
    "/search-use-create-test",
    # response_model=List[_test_schemas.TestDetail]
)
async def search_user_create(username: str):
    response = test_service.sreach_user_create_test(username)
    return response
