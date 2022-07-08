from app.utils.aws.dynamodb import table


def update_info_user(
    user_in: dict
):
    date = table.update_item(
        Key={
            "PK": user_in.get('pk'),
            "SK": user_in.get('sk')
        },
        UpdateExpression="SET #fn = :first_name, #ls = :last_name,\
                                #e = :email, #dob = :birth",
        ExpressionAttributeValues={
            ':first_name': user_in.get('first_name'),
            ':last_name': user_in.get('last_name'),
            ':email': user_in.get('email'),
            ':birth': str(user_in.get('dob')),
        },
        ExpressionAttributeNames={
            "#fn": "FirstName",
            "#ls": "LastName",
            "#e": "Email",
            "#dob": "DayOfBirth"
        },
        ReturnValues="UPDATED_NEW"
    )
    response = date.get('Attributes')
    response.update({
        "Username": user_in.get('username')
    })
    return response
