from app.models.domain import (
    base as _base_domain,
    type as _type_domain
)


class TypeCreate(
    _type_domain.NameType
):
    pass


class TypeDeatil(
    _base_domain.IdType, _type_domain.NameType
):
    pass
