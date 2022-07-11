from app.utils.aws.dynamodb import table
from boto3.dynamodb.conditions import Attr
from app.utils import report_status


def get_all_info_part(

) -> list:
    try:
        all_info_part = table.scan(
            FilterExpression=Attr('PK').begins_with('PART#')
        )
        return all_info_part['Items']
    except Exception:
        _ = report_status.get_exception("Part")
