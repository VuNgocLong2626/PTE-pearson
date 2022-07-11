from app.utils.aws.dynamodb import table
from boto3.dynamodb.conditions import Key
from app.utils import report_status


def get_part_by_id(
    pk: str,
    sk: str
) -> dict:
    try:
        info_part = table.query(
            KeyConditionExpression=Key("PK").eq(pk) &
            Key("SK").eq(sk)
        )
        respon = info_part["Items"][0]
        return respon
    except Exception:
        _ = report_status.get_exception("Part")
