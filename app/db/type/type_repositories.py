from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table


class TypeRepositories():

    def create_type(
        self,
        type_in: dict
    ):
        try:
            response = helpers.put_item_not_exists_PK_And_SK(type_in)
            return response
        except Exception:
            report_status.create_exception("Type")

    def delete_type(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_all_info_type(
        self
    ):
        try:
            all_info_type = table.scan(
                FilterExpression=Attr('PK').begins_with('TYPE#')
            )
            return all_info_type['Items']
        except Exception:
            _ = report_status.get_exception("Type")

    def get_info_by_id(
        self,
        pk: str,
        sk: str
    ):
        try:
            info_type = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            respon = info_type["Items"][0]
            return respon
        except Exception:
            _ = report_status.get_exception("Part")

    def update_type(
        self,
        type_in: dict
    ):
        _ = helpers.put_item(type_in)
