from pydantic import BaseModel, Field


class PartitionKey(BaseModel):
    pk: str = Field(..., alias="PK")


class SortKey(BaseModel):
    sk: str = Field(..., alias="SK")


class GlobalSecondaryIndexesPartitionKey(BaseModel):
    gsi1pk: str = Field(..., alias="gsi1pk")


class GlobalSecondaryIndexesSortKey(BaseModel):
    gsi1sk: str = Field(..., alias="gsi1sk")


class IdPart(BaseModel):
    id_part: str = Field(..., alias="IdPart")
