from app.utils.aws.dynamodb import table
from boto3.dynamodb.conditions import Key


def get_info_user(
    pk: str,
    sk: str
) -> dict:
    info_user = table.query(
        KeyConditionExpression=Key("PK").eq(pk) &
        Key("SK").eq(sk),
        Limit=1
    )
    respon = info_user["Items"]
    return respon
