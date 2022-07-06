from app.models.domain import (
    base as _base,
    part as _part_domain
)


class PartCreatInDB(
    _base.PartitionKey, _base.SortKey,
    _part_domain.Time, _part_domain.Title,
    _part_domain.PartName, _base.IdPart
):
    pass


class PartCreat(
    _part_domain.Time, _part_domain.Title,
    _part_domain.PartName
):
    pass


class PartDetail(
    _part_domain.Time, _part_domain.Title,
    _part_domain.PartName, _base.IdPart
):
    pass
