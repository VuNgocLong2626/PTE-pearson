from app.models.schemas import part as _part_schemas
from app.utils.aws.config_dynamodb import table


def create_part(
    part_in: _part_schemas.PartCreatInDB
) -> None:
    table.put_item(
        Item={
            **part_in.dict(by_alias=True),
            'Time': str(part_in.time)
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
