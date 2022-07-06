from app.utils.aws.config_dynamodb import table
from app.models.schemas import user as _user_domain


def create_user(
    user_in: _user_domain.UserCreateInDB
) -> None:
    table.put_item(
        Item={
            **user_in.dict(by_alias=True),
            'DayOfBirth': str(user_in.dob)
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
