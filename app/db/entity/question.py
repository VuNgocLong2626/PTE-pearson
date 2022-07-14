from app.models.schemas import question as _question_schemas
from app.db.entity.base import (
    BaseEntity,
    BaseGlobalSecondaryIndexesEntity
)
from ksuid import Ksuid


class QuestionEntity(
    BaseEntity, _question_schemas.QuestionDetail,
    BaseGlobalSecondaryIndexesEntity
):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        if not self.id_question:
            self.id_question = str(Ksuid())
        self.pk = f'QUESTION#{self.id_question}'
        self.sk = f'QUESTION#{self.id_question}'
        self.gsi1pk = f'TYPE#{self.id_type}'
        self.gsi1sk = f'QUESTION#{self.id_question}'

    def get_pk(id_question: str):
        pk = f'QUESTION#{id_question}'
        return pk

    def get_sk(id_question: str):
        sk = f'QUESTION#{id_question}'
        return sk

    def get_gsipk(id_type: str):
        gsipk = f'TYPE#{id_type}'
        return gsipk

    def get_gsisk(id_question: str):
        gsisk = f'TYPE#{id_question}'
        return gsisk

    def get_pk_and_sk(id_question: str):
        pk = QuestionEntity.get_pk(id_question)
        sk = QuestionEntity.get_sk(id_question)
        return pk, sk

    def get_gsipk_and_gsisk(id_type: str, id_question: str):
        gsipk = QuestionEntity.get_gsipk(id_type)
        gsisk = QuestionEntity.get_gsisk(id_question)
        return gsipk, gsisk

    def set_path(self, path: str):
        self.path = path
