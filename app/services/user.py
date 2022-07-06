from app.utils import report_status
from app.models.schemas import user as _user_schemas

from app.db.user.create_user \
    import create_user as query_create_user
from app.db.user.get_info_user \
    import get_info_user as query_get_info_user
from app.db.user.delete_user_by_username \
    import delete_user_by_username as query_delete_user_by_username
from app.db.user.update_info_user\
    import update_info_user as query_update_info_user


class UserService():

    def create_user(
        user_in: _user_schemas.UserCreate
    ) -> dict:
        try:
            db_in = {
                'PK': f"USER#{user_in.username}",
                'SK': f"USER#{user_in.username}",
                **user_in.dict(by_alias=True)
            }
            respon = _user_schemas.UserCreateInDB(**db_in)
            _ = query_create_user(respon)
            return respon
        except Exception:
            raise report_status.create_exception("User")

    def get_info_user(
        username: str
    ) -> _user_schemas.UserCreateInDB:
        try:
            respon = query_get_info_user(username)[0]
            return respon
        except Exception:
            report_status.get_exception("User")

    def delete_user_by_username(
        username: str
    ) -> None:
        check_username = query_get_info_user(username)
        if not check_username:
            report_status.get_exception("User")
        _ = query_delete_user_by_username(username)
        report_status.delete_done("User")

    def update_user_info(
        user_in: _user_schemas.UserUpdateInfo
    ) -> None:
        check_username = query_get_info_user(user_in.username)
        if not check_username:
            report_status.get_exception("User")
        db_in = {
            'PK': f"USER#{user_in.username}",
            'SK': f"USER#{user_in.username}",
            **user_in.dict(by_alias=True)
        }
        user_in_db = _user_schemas.UserUpdateInfoInDB(**db_in)
        _ = query_update_info_user(user_in_db)
        respon = query_get_info_user(user_in.username)[0]
        return respon
