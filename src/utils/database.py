"Conexão com o banco"

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from src.utils.settings import Settings

engine = create_engine(Settings().DATABASE_URL)

def get_session():
    "Cria uma sessão para acesso temporário ao banco"
    with Session(engine) as session:
        yield session
