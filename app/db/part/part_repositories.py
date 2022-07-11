from app.db.part.create_part \
    import create_part as _create_part
from app.db.part.delete_part_by_id \
    import delete_part_by_id as _delete_part
from app.db.part.get_part_by_id \
    import get_part_by_id as _get_info
from app.db.part.get_all_info_part \
    import get_all_info_part as _get_all_info_part


class PartRepositories():

    def create_part(
        slef,
        part_in: dict
    ) -> None:
        response = _create_part(part_in)
        return response

    def delete_part_by_id(
        self,
        pk: str,
        sk: str
    ) -> None:
        response = _delete_part(pk, sk)
        return response

    def get_info_part(
        self,
        pk: str,
        sk: str
    ) -> dict:
        response = _get_info(pk, sk)
        return response

    def get_all_info(
        self
    ) -> list:
        response = _get_all_info_part()
        return response
