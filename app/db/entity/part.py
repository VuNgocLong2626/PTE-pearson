from app.models.schemas import part as _part_schemas
from app.db.entity.base import BaseEntity
from ksuid import Ksuid


class PartEntity(
    BaseEntity, _part_schemas.PartCreatInDB
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.id_part = str(Ksuid())
        self.pk = f'PART#{self.id_part}'
        self.sk = f'PART#{self.id_part}'

    def get_pk(id_part: str):
        pk = f'PART#{id_part}'
        return pk

    def get_sk(id_part: str):
        sk = f'PART#{id_part}'
        return sk

    def get_pk_and_sk(id_part: str):
        pk = PartEntity.get_pk(id_part)
        sk = PartEntity.get_sk(id_part)
        return pk, sk
