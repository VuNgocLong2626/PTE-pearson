from app.utils.aws import helpers as _helpers


def create_user(
    user_in: dict
) -> None:
    response = _helpers.put_item_not_exists_PK_And_SK(user_in)
    return response
