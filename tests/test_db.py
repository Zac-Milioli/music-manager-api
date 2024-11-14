from src.models import Music
from sqlalchemy import select


class TestDB:
    def test_create_music(self, session):
        test_name = "testMusic"
        test_music = Music(name=test_name)

        session.add(test_music)
        session.commit()

        response = session.scalar(select(Music).where(Music.name == test_name))

        assert response.description == None
        assert response.type == None
        assert response.id == 1
        assert response.name == test_name
