from pydantic import BaseModel, Field


class PartitionKey(BaseModel):
    pk: str = Field(None, alias="PK")


class SortKey(BaseModel):
    sk: str = Field(None, alias="SK")


class GlobalSecondaryIndexesPartitionKey(BaseModel):
    gsi1pk: str = Field(None, alias="GSI1PK")


class GlobalSecondaryIndexesSortKey(BaseModel):
    gsi1sk: str = Field(None, alias="GSI1SK")


class IdPart(BaseModel):
    id_part: str = Field(None, alias="IdPart")


class IdQuestion(BaseModel):
    id_question: str = Field(None, alias="IdQuestion")


class IdType(BaseModel):
    id_type: str = Field(None, alias="IdType")
