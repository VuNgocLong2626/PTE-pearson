from app.db.user.create_user \
    import create_user as _create_user
from app.db.user.get_info_user \
    import get_info_user as _get_info_user
from app.db.user.delete_user_by_username \
    import delete_user_by_username as _delete_user_by_username
from app.db.user.update_info_user\
    import update_info_user as _update_info_user


class UserRepositories():

    def create_user(user_in: dict):
        response = _create_user(user_in)
        return response

    def get_info_user(pk: str, sk: str):
        response = _get_info_user(pk, sk)
        return response

    def delete_user_by_username(pk: str, sk: str):
        _ = _delete_user_by_username(pk, sk)

    def update_info_user(user_in: dict):
        response = _update_info_user(user_in)
        return response
