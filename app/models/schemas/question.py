from app.models.domain import question as _question_domain
from app.models.domain import base as _base_domain


class QuestionCreate(
    _question_domain.Title, _question_domain.Content,
    _question_domain.Path, _question_domain.Time
):
    pass


class QuestionDetail(
    _question_domain.Title, _question_domain.Content,
    _base_domain.IdQuestion, _question_domain.Path,
    _question_domain.Time
):
    pass


class QuestionUpdate(
    _question_domain.Title, _question_domain.Content,
    _base_domain.IdQuestion, _question_domain.Time
):
    pass
