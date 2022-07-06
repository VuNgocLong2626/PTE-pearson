from app.utils.aws.config_dynamodb import table


def delete_user_by_username(
    username: str
) -> None:
    _ = table.delete_item(
        Key={
            "PK": f"USER#{username}",
            "SK": f"USER#{username}"
        }
    )
