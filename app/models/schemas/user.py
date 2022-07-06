from app.models.domain import (
    base as _base,
    user as _user_domain
)


class UserCreateInDB(
    _base.PartitionKey, _base.SortKey,
    _user_domain.UserUsername, _user_domain.UserPassWord,
    _user_domain.LastName, _user_domain.FirstName,
    _user_domain.DayOfBirth, _user_domain.Email
):
    pass


class UserUpdateInfoInDB(
    _base.PartitionKey, _base.SortKey,
    _user_domain.LastName, _user_domain.FirstName,
    _user_domain.DayOfBirth, _user_domain.Email,
    _user_domain.UserUsername
):
    pass


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
