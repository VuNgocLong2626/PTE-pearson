from app.models.domain import (
    test as _test_domain,
    base as _base_domain
)
from app.models.schemas import (
    user as _user_schemas,
    part as _part_schemas,
    question as _question_schemas
)


class TestCreate(
    _test_domain.NameTest, _test_domain.Title,
    _test_domain.Time, _user_schemas.UserBasic
):
    pass


class TestDetail(
    _test_domain.NameTest, _test_domain.Title,
    _test_domain.Time, _test_domain.Scores,
    _base_domain.IdTest, _user_schemas.UserBasic
):
    pass


class TestDetailOfUserCreate(
    _test_domain.NameTest, _test_domain.Title,
    _test_domain.Time, _test_domain.Scores,
    _base_domain.IdTest
):
    pass


class TestMorePart(
    _part_schemas.PartDetail
):
    pass


class TestMorePartIn(
    _part_schemas.PartDetail, _base_domain.IdTest
):
    pass


class TestMoreQuestion(
    _question_schemas.QuestionDetail
):
    pass


class TestMoreQuestionIn(
    _question_schemas.QuestionDetail, _base_domain.IdPart,
    _base_domain.IdQuestion
):
    pass