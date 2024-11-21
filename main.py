"""Arquivo inicializador. Define as rotas e faz as conexões entre as funções"""

from http import HTTPStatus
from datetime import datetime
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.music_model import Music
from src.schemas.music_schema import MusicSchema, MusicPublic
from src.utils.database import get_session

app = FastAPI()
database = []


@app.get("/music", status_code=HTTPStatus.OK, response_model=list[MusicPublic])
def get_database(
    limit: int = 15, start_after: int = 0, session: Session = Depends(get_session)
):
    "Endpoint que retorna a base de dados parametrizada"
    musics = session.scalars(select(Music).limit(limit).offset(start_after))
    return musics

@app.get("/music/{music_id}", status_code=HTTPStatus.FOUND, response_model=MusicPublic)
def get_music(music_id: int, session: Session = Depends(get_session)):
    "Endpoint para busca de uma música específica"
    music_db = session.scalar(select(Music).where(Music.id == music_id))
    if not music_db:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="Music not found")
    
    return music_db

@app.post("/music", status_code=HTTPStatus.CREATED, response_model=MusicPublic)
def post_music(q: MusicSchema, session: Session = Depends(get_session)):
    "Endpoint referente à criação de Music"
    db_music = session.scalar(select(Music).where(Music.name == q.name))

    if db_music:
        raise HTTPException(HTTPStatus.CONFLICT, "Music already exists")

    db_music = Music(**q.model_dump())
    session.add(db_music)
    session.commit()
    session.refresh(db_music)

    return db_music


@app.put("/music/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def put_music(music_id: int, q: MusicSchema, session: Session = Depends(get_session)):
    "Endpoint referente à atualização de Music"
    music_db = session.scalar(select(Music).where(Music.id == music_id))
    if not music_db:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="Music not found")

    music_db.name = q.name
    music_db.description = q.description
    music_db.type = q.type
    
    session.add(music_db)
    session.commit()
    session.refresh(music_db)
    
    return music_db

@app.delete("/music/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def delete_music(music_id: int, session: Session = Depends(get_session)):
    "Endpoint referente à exclusão de Music"
    music_db = session.scalar(select(Music).where(Music.id == music_id))
    if not music_db:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="Music not found")

    session.delete(music_db)
    session.commit()

    return music_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
