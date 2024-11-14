"""Classes e funções referentes aos testes unitários do banco de dados"""

from sqlalchemy import select
from src.models import Music


class TestDB:
    "Classe de testes para a base de dados"

    def test_create_music(self, session):
        "Testa a criação de uma Music"
        test_name = "testMusic"
        test_music = Music(name=test_name)

        session.add(test_music)
        session.commit()

        response = session.scalar(select(Music).where(Music.name == test_name))

        assert response.description is None
        assert response.type is None
        assert response.id == 1
        assert response.name == test_name
