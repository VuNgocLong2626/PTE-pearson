from app.models.domain import (
    user as _user_domain
)


class UserCreate(
    _user_domain.UserUsername, _user_domain.UserPassWord,
    _user_domain.LastName, _user_domain.FirstName,
    _user_domain.DayOfBirth, _user_domain.Email
):
    pass


class UserDetail(
    _user_domain.LastName, _user_domain.FirstName,
    _user_domain.DayOfBirth, _user_domain.Email,
    _user_domain.UserUsername
):
    pass


class UserUpdateInfo(
    _user_domain.LastName, _user_domain.FirstName,
    _user_domain.DayOfBirth, _user_domain.Email,
    _user_domain.UserUsername
):
    pass


class UserBasic(
    _user_domain.UserUsername
):
    pass
