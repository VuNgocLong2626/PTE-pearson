from app.models.schemas.test import TestMorePart
from app.db.entity import base as _base_entity


class TestPartEntity(
    _base_entity.BaseEntity, TestMorePart
):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.pk = f'TEST#{kwargs.get("IdTest", None)}'
        self.sk = f'PART#{self.id_part}'

    def get_pk(id_test: str):
        pk = f'TEST#{id_test}'
        return pk

    def get_sk(id_test: str):
        sk = f'PART#{id_test}'
        return sk

    def get_pk_and_sk(id_test: str):
        pk = TestPartEntity.get_pk(id_test)
        sk = TestPartEntity.get_sk(id_test)
        return pk, sk
