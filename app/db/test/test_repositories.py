from app.utils.aws import helpers
from app.utils import report_status
from boto3.dynamodb.conditions import Key, Attr
from app.utils.aws.dynamodb import table


class TestRespositories():

    def creat_test(
        self,
        test_in: dict
    ) -> None:
        try:
            helpers.put_item_not_exists_PK_And_SK(test_in)
            return {'message': 'create successfully'}
        except Exception:
            report_status.create_exception('Test')

    def get_all_test_info(
        self
    ):
        try:
            info_test = table.scan(
                FilterExpression=Attr('PK').begins_with('TEST#')
            )
            response = info_test['Items']
            return response
        except Exception:
            report_status.get_exception('Test')

    def get_test_info_by_id(
        self,
        pk: str,
        sk: str,
    ):
        try:
            info_test = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            response = info_test['Items'][0]
            return response
        except Exception:
            report_status.get_exception('Test')
