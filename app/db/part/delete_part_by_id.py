from app.utils.aws.helpers import delete_item


def delete_part_by_id(
    pk: str,
    sk: str
) -> None:
    _ = delete_item(pk, sk)
