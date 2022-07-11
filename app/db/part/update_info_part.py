from app.utils.aws.helpers import put_item


def update_part(
    part_in: dict
) -> None:
    _ = put_item(part_in)
