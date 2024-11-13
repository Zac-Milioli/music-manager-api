from schemas import MusicSchema, MusicPublic
from datetime import datetime
from http import HTTPStatus
from fastapi import FastAPI
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
            date=datetime.strftime(datetime.now(), "%d/%m/%Y"),
            id=len(database)+1
            )
    database.append(music_refactor)
    return music_refactor

@app.put("/music/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def put_music(music_id: int, q: MusicSchema):
    music_refactor = MusicPublic(
            **q.model_dump(),
            date=datetime.strftime(datetime.now(), "%d/%m/%Y"),
            id=music_id
            )
    database[music_id-1] = music_refactor
    return music_refactor


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)