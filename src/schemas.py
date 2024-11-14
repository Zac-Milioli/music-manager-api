"""Classes e funções referentes às trocas da API"""

from pydantic import BaseModel


class MusicSchema(BaseModel):
    "Schema para Music na criação"
    name: str
    description: str
    type: str


class MusicPublic(MusicSchema):
    "Schema para Music quando é incluída no banco de dados"
    id: int
    created_at: str
