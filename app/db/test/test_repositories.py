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
    ) -> list:
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
    ) -> dict:
        try:
            info_test = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            response = info_test['Items'][0]
            return response
        except Exception:
            report_status.get_exception('Test')

    def update_test(
        self,
        test_info: dict
    ) -> None:
        _ = helpers.put_item(test_info)

    def sreach_user_create_test(
        self,
        gsi1pk: str
    ) -> list:
        try:
            info_test = table.query(
                IndexName="GSI1",
                KeyConditionExpression=Key("GSI1PK").eq(gsi1pk)
            )
            response = info_test['Items']
            return response
        except Exception:
            report_status.get_exception('Test')

    def more_part_to_the_test(
        self,
        part_in: dict
    ):
        try:
            _ = helpers.put_item_not_exists_PK(part_in)
        except Exception:
            _ = report_status.create_exception('More Part')

