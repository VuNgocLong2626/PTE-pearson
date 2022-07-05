from pydantic import BaseModel, Field


class NamePermission(BaseModel):
    name_permission: str = Field(..., alias="name_permission")
