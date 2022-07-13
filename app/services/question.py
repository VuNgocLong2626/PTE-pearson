from fastapi import UploadFile

from app.models.schemas import question as _question_schemas
from app.db.entity import question as _question
from app.utils.aws import s3 as _aws_s3
from app.db.question.question_repositories import QuestionRepositories


question_repositories = QuestionRepositories()


class QuestionService():

    def create_question(
        self,
        question_in: _question_schemas.QuestionCreate,
        file: UploadFile
    ) -> dict:
        question = _question.QuestionEntity(**question_in.dict(by_alias=True))
        file_name = _aws_s3.get_file_name(file.filename, question.id_question)
        question.set_path(file_name)
        _ = _aws_s3.upload_file(file, file_name)
        _ = question_repositories.create_question(question.dict(by_alias=True))
        return question

    def get_info_by_id(
        self,
        id_question: str
    ):
        pk, sk=_question.QuestionEntity.get_pk_and_sk(id_question)

        return pk

    def get_file(
        self
    ):
        response = _aws_s3.create_presigned_url(
            'toiec.mp3'
        )
        print(type(response))
        return response

    def detete_file(
        self
    ):
        response = _aws_s3.delete_file('2BpvnRPLYn1bZZluKr8bn5GSIpT.mp3')
        return response
