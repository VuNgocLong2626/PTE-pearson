from fastapi import UploadFile

from app.models.schemas import question as _question_schemas
from app.db.entity import question as _question
from app.utils.aws import s3 as _aws_s3
from app.db.question.question_repositories import QuestionRepositories
from app.services.type import TypeService


question_repositories = QuestionRepositories()
type_service = TypeService()


class QuestionService():

    def create_question(
        self,
        question_in: _question_schemas.QuestionCreate,
        file: UploadFile
    ) -> None:
        _ = type_service.get_info_type_by_id(question_in.id_type)
        question = _question.QuestionEntity(**question_in.dict(by_alias=True))
        file_name = _aws_s3.get_file_name(file.filename, question.id_question)
        question.set_path(file_name)
        _ = _aws_s3.upload_file(file, file_name)
        _ = question_repositories.create_question(question.dict(by_alias=True))
        return {'message': 'create successfully'}

    def get_info_question_by_id(
        self,
        id_question: str
    ) -> dict:
        pk, sk = _question.QuestionEntity.get_pk_and_sk(id_question)
        response = question_repositories.get_info_question_by_id(pk, sk)

        presigned_url = _aws_s3.create_presigned_url(response.get('Path'))
        response.update({
            'Path': presigned_url
        })
        return response

    def search_question_by_id_type(
        self,
        id_type: str
    ) -> list:
        _ = type_service.get_info_type_by_id(id_type)
        gsi1pk = _question.QuestionEntity.get_gsipk(id_type)
        response = question_repositories.search_question_by_type(gsi1pk)
        return response

    def delete_question(
        self,
        id_question: str
    ):
        question = self.get_info_question_by_id(id_question)
        _ = question_repositories.delete_question(
            question.get('pk'),
            question.get('sk')
        )
        path = question.get('path')
        _ = _aws_s3.delete_file(path)
        return {'message': 'delete successfully'}

    def check_question(
        self,
        id_question: str
    ) -> None:
        pk, sk = _question.QuestionEntity.get_pk_and_sk(id_question)
        _ = question_repositories.get_info_question_by_id(pk, sk)

    def update_question(
        self,
        question_in: _question_schemas.QuestionUpdate,
        file: UploadFile
    ):
        _ = self.check_question(question_in.id_question)
        _ = type_service.get_info_type_by_id(question_in.id_type)

        question = _question.QuestionEntity(**question_in.dict(by_alias=True))
        file_name = _aws_s3.get_file_name(file.filename, question.id_question)
        _ = _aws_s3.delete_file(file_name)
        _ = _aws_s3.upload_file(file, file_name)
        question.set_path(file_name)
        _ = question_repositories.update_question(question.dict(by_alias=True))
        return {'message': 'update successfully'}

    def get_info_by_id(
        self,
        id_question: str
    ):
        pk, sk = _question.QuestionEntity.get_pk_and_sk(id_question)

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
        response = _aws_s3.delete_file('toiec.mp3')
        return response
