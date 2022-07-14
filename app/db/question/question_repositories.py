from app.utils.aws import helpers
from app.utils import report_status
from boto3.dynamodb.conditions import Key
from app.utils.aws.dynamodb import table


class QuestionRepositories():

    def create_question(
        self,
        question_in: dict
    ) -> None:
        try:
            response = helpers.put_item(question_in)
            return response
        except Exception:
            _ = report_status.create_exception("Question")

    def delete_question(
        self,
        pk: str,
        sk: str
    ) -> None:
        _ = helpers.delete_item(pk, sk)

    def get_info_question_by_id(
        self,
        pk: str,
        sk: str
    ) -> dict:
        try:
            info_question = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            response = info_question['Items'][0]
            return response
        except Exception:
            report_status.get_exception('Question')

    def search_question_by_type(
        self,
        pk
    ):
        try:
            info_question = table.query(
                IndexName="GSI1",
                KeyConditionExpression=Key("GSI1PK").eq(pk)
            )
            response = info_question['Items']
            return response
        except Exception:
            report_status.get_exception('Question')

    def update_question(
        self,
        question_in: dict
    ) -> None:
        _ = helpers.put_item(question_in)
