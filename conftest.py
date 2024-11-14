from main import app
from fastapi.testclient import TestClient
from src.models import table_registry
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pytest

@pytest.fixture()
def client():
    return TestClient(app)

@pytest.fixture()
def session():
    engine = create_engine(f"sqlite:///:memory:")
    table_registry.metadata.create_all(engine)

    # Executa os testes da fixture aqui
    with Session(engine) as session:
        yield session
    
    # Código executado ao encerrar o teste com a fixture
    table_registry.metadata.drop_all(engine)
