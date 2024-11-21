"""Classes e funções referentes às trocas da API"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MusicSchema(BaseModel):
    "Schema para Music na criação"
    name: str
    description: str | None = None
    type: str | None = None
    model_config = ConfigDict(from_attributes=True)


class MusicPublic(MusicSchema):
    "Schema para Music quando é incluída no banco de dados"
    id: int
    created_at: datetime
