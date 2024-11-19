"""Classes e funções referentes às trocas da API"""

from pydantic import BaseModel
from datetime import datetime


class MusicSchema(BaseModel):
    "Schema para Music na criação"
    name: str
    description: str | None = None
    type: str | None = None


class MusicPublic(MusicSchema):
    "Schema para Music quando é incluída no banco de dados"
    id: int
    created_at: datetime
