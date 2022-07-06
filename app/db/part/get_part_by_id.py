from app.models.schemas import part as _part_schemas
from app.utils.aws.config_dynamodb import table
from boto3.dynamodb.conditions import Key


def get_part_by_id(id_part: str):
    info_part = table.query(
        KeyConditionExpression=Key("PK").eq(f"PART#{id_part}") &
        Key("SK").eq(f"PART#{id_part}")
    )
    respon = info_part["Items"]
    return respon
