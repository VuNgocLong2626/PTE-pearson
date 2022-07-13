from app.models.schemas import type as _type_schemas
from app.db.entity.base import BaseEntity
from ksuid import Ksuid


class TypeEntity(
    BaseEntity, _type_schemas.TypeDeatil
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        if not self.id_type:
            self.id_type = str(Ksuid())
        self.pk = f'TYPE#{self.id_type}'
        self.sk = f'TYPE#{self.id_type}'

    def get_pk(id_type: str):
        pk = f'TYPE#{id_type}'
        return pk

    def get_sk(id_type: str):
        sk = f'TYPE#{id_type}'
        return sk

    def get_pk_and_sk(id_type: str):
        pk = TypeEntity.get_pk(id_type)
        sk = TypeEntity.get_sk(id_type)
        return pk, sk
