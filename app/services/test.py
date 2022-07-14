from app.models.schemas import test as _test_schemas
from app.db.entity import test as _test
from app.db.test.test_repositories import TestRespositories
from app.services.user import UserService


test_respositories = TestRespositories()
user_services = UserService()


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
        self.check_test_info(test_in.id_test)
        test = _test.TestEntity(**test_in.dict(by_alias=True))
        _ = test_respositories.update_test(test.dict(by_alias=True))
        return {'message': 'update successfully'}
