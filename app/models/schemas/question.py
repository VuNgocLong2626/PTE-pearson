from app.models.domain import (
    question as _question_domain,
    base as _base_domain
)
from app.models.schemas import type as _type_schemas


class QuestionCreate(
    _question_domain.Title, _question_domain.Content,
    _question_domain.Path, _question_domain.Time,
    _type_schemas.TypeDeatil
):
    pass


class QuestionDetail(
    _question_domain.Title, _question_domain.Content,
    _base_domain.IdQuestion, _question_domain.Path,
    _question_domain.Time, _type_schemas.TypeDeatil
):
    pass


class QuestionUpdate(QuestionDetail):
    pass
