from app.models.schemas import test as _test_schemas
from app.db.test.test_repositories import TestRespositories
from app.services.user import UserService
from app.db.entity import (
    test as _test,
    test_part as _test_part
)
from app.services.part import PartService


test_respositories = TestRespositories()
user_services = UserService()
part_services = PartService()


class TestService():

    def create_test(
        self,
        test_in: _test_schemas.TestCreate
    ) -> dict:
        user_services.get_info_user(test_in.username)
        test = _test.TestEntity(**test_in.dict(by_alias=True))
        response = test_respositories.creat_test(test.dict(by_alias=True))
        return response

    def get_all_info_test(
        self
    ) -> list:
        response = test_respositories.get_all_test_info()
        return response

    def get_test_info_by_id(
        self,
        id_test: str
    ) -> dict:
        pk, sk = _test.TestEntity.get_pk_and_sk(id_test)
        response = test_respositories.get_test_info_by_id(pk, sk)
        return response

    def check_test_info(
        self,
        id_test: str
    ) -> None:
        pk, sk = _test.TestEntity.get_pk_and_sk(id_test)
        _ = test_respositories.get_test_info_by_id(pk, sk)

    def update_test(
        self,
        test_in: _test_schemas.TestDetail
    ) -> dict:
        user_services.get_info_user(test_in.username)
        self.check_test_info(test_in.id_test)
        test = _test.TestEntity(**test_in.dict(by_alias=True))
        _ = test_respositories.update_test(test.dict(by_alias=True))
        return {'message': 'update successfully'}

    def sreach_user_create_test(
        self,
        username: str
    ) -> dict:
        response = {}
        gsi1pk = _test.TestEntity.get_gsipk(username)
        test_all = test_respositories.sreach_user_create_test(gsi1pk)
        list_test = list(
            map(lambda item: _test_schemas.TestDetailOfUserCreate(**item),
                test_all)
        )
        response.update({
            'Username': username,
            'ListTest': list_test
        })
        return response

    def more_part(
        self,
        part_in: _test_schemas.TestMorePartIn
    ):
        self.check_test_info(part_in.id_test)
        part_services.get_info_part(part_in.id_part)

        part = _test_part.TestPartEntity(**part_in.dict(by_alias=True))
        _ = test_respositories.more_part_to_the_test(part.dict(by_alias=True))
        return {'message': 'more part successfully'}
