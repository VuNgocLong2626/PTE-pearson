from app.utils import report_status
from app.models.schemas import user as _user_schemas
from app.db.entity import user as _user
from app.db.user.user_repositories import UserRepositories


user_repositories = UserRepositories


class UserService():

    def create_user(
        self,
        user_in: _user_schemas.UserCreate
    ) -> dict:
        try:
            user = _user.UserEntity(**user_in.dict(by_alias=True))
            _ = user_repositories.create_user(user.dict(by_alias=True))
            return user_in
        except Exception:
            _ = report_status.create_exception("User")

    def get_info_user(
        self,
        username: str
    ) -> dict:
        try:
            pk, sk = _user.UserEntity.get_pk_and_sk(username)
            response = user_repositories.get_info_user(
                pk, sk
            )[0]
            return response
        except Exception:
            report_status.get_exception("User")

    def delete_user_by_username(
        self,
        username: str
    ) -> None:
        self.get_info_user(username)
        pk, sk = _user.UserEntity.get_pk_and_sk(username)
        _ = user_repositories.delete_user_by_username(
            pk, sk
        )
        report_status.delete_done("User")

    def update_user_info(
        self,
        user_in: _user_schemas.UserUpdateInfo
    ) -> _user_schemas.UserDetail:
        user = _user.UserEntity(**user_in.dict(by_alias=True))
        _ = self.get_info_user(user.username)
        response = user_repositories.update_info_user(user.dict())
        return response
