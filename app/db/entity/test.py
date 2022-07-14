from app.models.schemas.test import TestDetail
from app.models.schemas.user import UserBasic
from app.db.entity import base as _base_entity
from ksuid import Ksuid


class TestEntity(
    TestDetail, _base_entity.BaseEntity,
    _base_entity.BaseGlobalSecondaryIndexesEntity,
    UserBasic
):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        if not self.id_test:
            self.id_test = str(Ksuid())
        self.pk = f'TEST#{self.id_test}'
        self.sk = f'TEST#{self.id_test}'
        self.gsi1pk = f'USER#{self.username}'
        self.gsi1sk = f'TEST#{self.id_test}'

    def get_pk(id_test: str):
        pk = f'TEST#{id_test}'
        return pk

    def get_sk(id_test: str):
        sk = f'TEST#{id_test}'
        return sk

    def get_gsipk(username: str):
        gsipk = f'USER#{username}'
        return gsipk

    def get_gsisk(id_test: str):
        gsisk = f'TEST#{id_test}'
        return gsisk

    def get_pk_and_sk(id_test: str):
        pk = TestEntity.get_pk(id_test)
        sk = TestEntity.get_sk(id_test)
        return pk, sk

    def get_gsipk_and_gsisk(id_test: str, username: str):
        gsipk = TestEntity.get_gsipk(id_test)
        gsisk = TestEntity.get_gsisk(username)
        return gsipk, gsisk
