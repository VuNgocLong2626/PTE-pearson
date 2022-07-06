from app.utils import report_status
from ksuid import Ksuid
from app.models.schemas import part as _part_schemas

from app.db.part.create_part import create_part as query_create_part


class PartService():

    def create_part(
        part_in: _part_schemas.PartCreat
    ) -> _part_schemas.PartCreatInDB:
        id_part = str(Ksuid())
        db_in = {
            'PK': f"PART#{id_part}",
            'SK': f"PART#{id_part}",
            **part_in.dict(by_alias=True),
            'IdPart': id_part
        }
        respon = _part_schemas.PartCreatInDB(**db_in)
        _ = query_create_part(respon)
        return respon
