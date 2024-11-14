from src.schemas import MusicSchema, MusicPublic
from datetime import datetime
from http import HTTPStatus
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()
database = []


@app.get("/music", status_code=HTTPStatus.OK, response_model=list[MusicPublic])
def get_database():
    return database


@app.post("/music", status_code=HTTPStatus.CREATED, response_model=MusicPublic)
def post_music(q: MusicSchema):
    music_refactor = MusicPublic(
        **q.model_dump(),
        created_at=datetime.strftime(datetime.now(), "%d/%m/%Y"),
        id=len(database) + 1
    )
    database.append(music_refactor)
    return music_refactor


@app.put("/music/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def put_music(music_id: int, q: MusicSchema):
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
    if music_id > len(database) or music_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Music not found")

    data = database.pop(music_id - 1)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
