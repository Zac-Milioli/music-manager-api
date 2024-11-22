from fastapi import APIRouter
from http import HTTPStatus
from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.music_model import Music
from src.schemas.music_schema import MusicSchema, MusicPublic
from src.utils.database import get_session

router = APIRouter(prefix="/music", tags=["music"])


@router.get("/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def get_music(music_id: int, session: Session = Depends(get_session)):
    "Endpoint para busca de uma música específica"
    music_db = session.scalar(select(Music).where(Music.id == music_id))
    if not music_db:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="Music not found")

    return music_db


@router.post("/", status_code=HTTPStatus.CREATED, response_model=MusicPublic)
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


@router.put("/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
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


@router.delete("/{music_id}", status_code=HTTPStatus.OK, response_model=MusicPublic)
def delete_music(music_id: int, session: Session = Depends(get_session)):
    "Endpoint referente à exclusão de Music"
    music_db = session.scalar(select(Music).where(Music.id == music_id))
    if not music_db:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="Music not found")

    session.delete(music_db)
    session.commit()

    return music_db
