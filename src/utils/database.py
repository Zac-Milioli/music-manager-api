"Conexão com o banco"

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from src.utils.settings import Settings


def get_engine(): # pragma: no cover
    "Cria a engine do ORM"
    return create_engine(Settings().DATABASE_URL)


def get_session(): # pragma: no cover
    "Cria uma sessão para acesso temporário ao banco"
    with Session(get_engine()) as session:
        yield session
