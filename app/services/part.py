from app.models.schemas import part as _part_schemas
from app.db.entity import part as _part
from app.db.part.part_repositories import PartRepositories


part_repositories = PartRepositories()


class PartService():

    def create_part(
        self,
        part_in: _part_schemas.PartCreat
    ) -> None:
        part = _part.PartEntity(**part_in.dict(by_alias=True))
        _ = part_repositories.create_part(part.dict(by_alias=True))
        return part

    def delete_part(
        self,
        id_part: str,
    ) -> None:
        self.get_info_part(id_part)
        pk, sk = _part.PartEntity.get_pk_and_sk(id_part)
        _ = part_repositories.delete_part_by_id(
            pk, sk
        )
        return {'message': 'Delete successfully'}

    def get_info_part(
        self,
        id_part
    ) -> dict:
        pk, sk = _part.PartEntity.get_pk_and_sk(id_part)
        response = part_repositories.get_info_part(
            pk, sk
        )
        return response

    def get_all_info_part(
        self
    ) -> list:
        response = part_repositories.get_all_info()
        return response

    def update_part(
        self,
        part_in: _part_schemas.PartDetail
    ):
        part = _part.PartEntity(**part_in.dict(by_alias=True))
        self.get_info_part(part.id_part)
        _ = part_repositories.update_part(part.dict(by_alias=True))
        return {'message': 'Update successfully'}
