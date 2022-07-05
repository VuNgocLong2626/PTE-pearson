from pydantic import BaseModel, Field


class PartitionKey(BaseModel):
    pk: str = Field(..., alias="pk")


class SortKey(BaseModel):
    sk: str = Field(..., alias="sk")


class GlobalSecondaryIndexesPartitionKey(BaseModel):
    gsi1pk: str = Field(..., alias="gsi1pk")


class GlobalSecondaryIndexesSortKey(BaseModel):
    gsi1sk: str = Field(..., alias="gsi1sk")
