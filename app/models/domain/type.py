from pydantic import BaseModel, Field


class NameType(BaseModel):
    name_type: str = Field(..., alias="NameType")
