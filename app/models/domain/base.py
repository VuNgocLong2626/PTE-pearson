from pydantic import BaseModel, Field


class PartitionKey(BaseModel):
    pk: str = Field(..., alias="PK")


class SortKey(BaseModel):
    sk: str = Field(..., alias="SK")


class GlobalSecondaryIndexesPartitionKey(BaseModel):
    gsi1pk: str = Field(..., alias="GSI1PK")


class GlobalSecondaryIndexesSortKey(BaseModel):
    gsi1sk: str = Field(..., alias="GSI1SK")
