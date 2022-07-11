from app.utils.aws.helpers \
    import put_item_not_exists_PK_And_SK as put_item
from app.utils import report_status


def create_part(
    part_in: dict
) -> None:
    try:
        response = put_item(part_in)
        return response
    except Exception:
        _ = report_status.create_exception("Part")
