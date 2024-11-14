from main import app
from fastapi.testclient import TestClient
from src.models import table_registry
from sqlalchemy import create_engine
import pytest

@pytest.fixture()
def client():
    return TestClient(app)

@pytest.fixture()
def connection():
    # Cria o database e inicializa a engine
    engine = create_engine(f"sqlite:///:memory:")
    table_registry.metadata.create_all(engine)
    return engine
