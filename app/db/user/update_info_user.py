from app.utils.aws.config_dynamodb import table
from app.models.schemas import user as _user_domain


def update_info_user(
    user_in: _user_domain.UserUpdateInfoInDB
):
    respon = table.update_item(
        Key={
            "PK": user_in.pk,
            "SK": user_in.sk
        },
        UpdateExpression="SET #fn = :first_name, #ls = :last_name,\
                                #e = :email, #dob = :birth",
        ExpressionAttributeValues={
            ':first_name': user_in.first_name,
            ':last_name': user_in.last_name,
            ':email': user_in.email,
            ':birth': str(user_in.dob),
        },
        ExpressionAttributeNames={
            "#fn": "FirstName",
            "#ls": "LastName",
            "#e": "Email",
            "#dob": "DayOfBirth"
        },
        ReturnValues="UPDATED_NEW"
    )
    return respon
