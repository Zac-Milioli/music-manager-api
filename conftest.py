"""Definição de fixtures para os testes unitários"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
import pytest
from src.models.music_model import table_registry
from src.utils.database import get_session
from main import app

@pytest.fixture()
def client(session):
    "Define e retorna o cliente de testes do FastAPI"
    def get_session_override():
        return session
    
    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture()
def session():
    """
    Define a engine em memória, constrói as
    tabelas e retorna a sessão, excluindo tudo ao fim
    """
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
        )
    table_registry.metadata.create_all(engine)

    # Executa os testes da fixture aqui
    with Session(engine) as temp_session:
        yield temp_session

    # Código executado ao encerrar o teste com a fixture
    table_registry.metadata.drop_all(engine)
