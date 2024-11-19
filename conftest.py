"""Definição de fixtures para os testes unitários"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pytest
from models.music_model import table_registry
from no_db_main import app


@pytest.fixture()
def client() -> TestClient:
    "Define e retorna o cliente de testes do FastAPI"
    return TestClient(app)


@pytest.fixture()
def session():
    """
    Define a engine em memória, constrói as
    tabelas e retorna a sessão, excluindo tudo ao fim
    """
    engine = create_engine("sqlite:///:memory:")
    table_registry.metadata.create_all(engine)

    # Executa os testes da fixture aqui
    with Session(engine) as temp_session:
        yield temp_session

    # Código executado ao encerrar o teste com a fixture
    table_registry.metadata.drop_all(engine)
