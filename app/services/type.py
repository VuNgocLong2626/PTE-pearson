from app.models.schemas import type as _type_schmeas
from app.db.type.type_repositories import TypeRepositories
from app.db.entity import type as _type


type_repositories = TypeRepositories()


class TypeService():

    def create_type(
        self,
        type_in: _type_schmeas.TypeCreate
    ):
        type = _type.TypeEntity(**type_in.dict(by_alias=True))
        _ = type_repositories.create_type(type.dict(by_alias=True))
        return {'message': 'create successfully'}

    def get_all_info(
        self
    ):
        response = type_repositories.get_all_info_type()
        return response

    def get_info_type_by_id(
        self,
        id_type: str
    ):
        pk, sk = _type.TypeEntity.get_pk_and_sk(id_type)
        response = type_repositories.get_info_by_id(pk, sk)
        return response

    def delete_type(
        self,
        id_type: str
    ):
        self.get_info_type_by_id(id_type)
        pk, sk = _type.TypeEntity.get_pk_and_sk(id_type)
        _ = type_repositories.delete_type(pk, sk)
        return {'message': 'delete successfully'}

    def update_type(
        self,
        type_in: _type_schmeas.TypeDeatil
    ):
        self.get_info_type_by_id(type_in.id_type)
        type = _type.TypeEntity(**type_in.dict(by_alias=True))
        _ = type_repositories.update_type(type.dict(by_alias=True))
        return {'message': 'update successfully'} 