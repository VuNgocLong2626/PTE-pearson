
from app.models.domain import base as _base_domain


class BaseEntity(
    _base_domain.PartitionKey,
    _base_domain.SortKey
):
    pass
