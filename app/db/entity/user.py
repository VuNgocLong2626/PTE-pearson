from app.models.schemas import user as _user_schemas
from app.db.entity.base import BaseEntity


class UserEntity(
    BaseEntity, _user_schemas.UserCreate
):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.pk = f'USER#{self.username}'
        self.sk = f'USER#{self.username}'

    def get_pk(username: str):
        pk = f'USER#{username}'
        return pk

    def get_sk(username: str):
        sk = f'USER#{username}'
        return sk

    def get_pk_and_sk(username: str):
        pk = UserEntity.get_pk(username)
        sk = UserEntity.get_sk(username)
        return pk, sk
