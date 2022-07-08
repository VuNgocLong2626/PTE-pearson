from app.utils.aws.helpers import delete_item


def delete_user_by_username(
    pk: str,
    sk: str
) -> None:
    _ = delete_item(pk, sk)
