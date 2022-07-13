from app.utils.aws import helpers
from app.utils import report_status


class QuestionRepositories():

    def create_question(
        self,
        question_in: dict
    ):
        try:
            response = helpers.put_item(question_in)
            return response
        except Exception:
            _ = report_status.create_exception("Question")
