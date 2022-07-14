from app.models.domain import (
    test as _test_domain,
    base as _base_domain
)
from app.models.schemas import user as _user_schemas


class TestCreate(
    _test_domain.NameTest, _test_domain.Title,
    _test_domain.Time, _user_schemas.UserBasic
):
    pass


class TestDetail(
    _test_domain.NameTest, _test_domain.Title,
    _test_domain.Time, _test_domain.Scores,
    _base_domain.IdTest
):
    pass
