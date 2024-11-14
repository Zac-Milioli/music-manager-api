from main import app
from fastapi.testclient import TestClient
from src.models import table_registry
from sqlalchemy import create_engine
from glob import glob
from os import remove
import pytest

@pytest.fixture()
def client():
    return TestClient(app)

@pytest.fixture()
def connection():
    database_path = r'tests/test_database.db'

    # Remove o arquivo database para testar com um arquivo novo
    globed = glob(database_path)
    if len(globed) == 1:
        remove(database_path)

    # Cria o database e inicializa a engine
    engine = create_engine(f"sqlite:///{database_path}")
    table_registry.metadata.create_all(engine)
    return engine
