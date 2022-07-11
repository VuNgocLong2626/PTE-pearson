from app.models.domain import (
    base as _base,
    part as _part_domain
)


class PartCreat(
    _part_domain.Time, _part_domain.Title,
    _part_domain.PartName
):
    pass


class PartCreatInDB(
    _part_domain.Time, _part_domain.Title,
    _part_domain.PartName, _base.IdPart
):
    pass


class PartDetail(
    _part_domain.Time, _part_domain.Title,
    _part_domain.PartName, _base.IdPart
):
    pass
