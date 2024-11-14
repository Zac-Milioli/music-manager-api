from pydantic import BaseModel

class MusicSchema(BaseModel):
    name: str
    description: str
    type: str

class MusicPublic(MusicSchema):
    id: int
    created_at: str
