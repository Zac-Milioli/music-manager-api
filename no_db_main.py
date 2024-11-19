"""Versão que não utiliza uma database real, apenas uma simulação"""

from http import HTTPStatus
from datetime import datetime
import uvicorn
from fastapi import FastAPI, HTTPException
from src.schemas.music_schema import MusicSchema, MusicPublic

app = FastAPI()
database = []


@app.get("/music", status_code=HTTPStatus.OK, response_model=list[MusicPublic])
def get_database():
    "Endpoint que retorna a base de dados completa"
    return database


@app.post("/music", status_code=HTTPStatus.CREATED, response_model=MusicPublic)
def post_music(q: MusicSchema):
    "Endpoint referente à criação de Music"
    music_refactor = MusicPublic(
        **q.model_dump(),
        created_at=datetime.strftime(datetime.now(), "%d/%m/%Y"),
        id=len(database) + 1
    )
    database.append(music_refactor)
    return music_refactor


@app.put("/music/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def put_music(music_id: int, q: MusicSchema):
    "Endpoint referente à atualização de Music"
    if music_id > len(database) or music_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Music not found")

    music_refactor = MusicPublic(
        **q.model_dump(),
        created_at=datetime.strftime(datetime.now(), "%d/%m/%Y"),
        id=music_id
    )
    database[music_id - 1] = music_refactor
    return music_refactor


@app.delete("/music/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def delete_music(music_id: int):
    "Endpoint referente à exclusão de Music"
    if music_id > len(database) or music_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Music not found")

    data = database.pop(music_id - 1)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
