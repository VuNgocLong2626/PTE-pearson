from app.utils.aws.config_dynamodb import table
from app.models.schemas import user as _user_domain
from boto3.dynamodb.conditions import Key


def get_info_user(
    username: str
) -> _user_domain.UserCreateInDB:
    info_user = table.query(
        KeyConditionExpression=Key("PK").eq(f"USER#{username}") &
        Key("SK").eq(f"USER#{username}")
    )
    respon = info_user["Items"]
    return respon
