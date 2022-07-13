from app.models.schemas import question as _question_schemas
from app.db.entity.base import BaseEntity
from ksuid import Ksuid


class QuestionEntity(
    BaseEntity, _question_schemas.QuestionDetail
):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        if not self.id_question:
            self.id_question = str(Ksuid())
        self.pk = f'QUESTION#{self.id_question}'
        self.sk = f'QUESTION#{self.id_question}'

    def get_pk(id_question: str):
        pk = f'QUESTION#{id_question}'
        return pk

    def get_sk(id_question: str):
        sk = f'QUESTION#{id_question}'
        return sk

    def get_pk_and_sk(id_question: str):
        pk = QuestionEntity.get_pk(id_question)
        sk = QuestionEntity.get_sk(id_question)
        return pk, sk

    def set_path(self, path: str):
        self.path = path
