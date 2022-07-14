from typing import List
from fastapi import APIRouter

from app.services.test import TestService
from app.models.schemas import test as _test_schemas


router = APIRouter()
test_service = TestService()


@router.post(
    "/create-test",
    # response_model=_test_schemas.TestDetail
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
