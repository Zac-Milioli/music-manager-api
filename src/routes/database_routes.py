from fastapi import APIRouter
from http import HTTPStatus
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.music_model import Music
from src.schemas.music_schema import MusicPublic
from src.utils.database import get_session

router = APIRouter(prefix="/music", tags=["database"])


@router.get("/", status_code=HTTPStatus.OK, response_model=list[MusicPublic])
def get_database(
    limit: int = 15, start_after: int = 0, session: Session = Depends(get_session)
):
    "Endpoint que retorna a base de dados parametrizada"
    musics = session.scalars(select(Music).limit(limit).offset(start_after))
    return musics
