from src.models import Music, table_registry
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

class TestDB:
    def test_create_music(self, connection):
        with Session(connection) as session:
            test_name = "testMusic"
            test_music = Music(
                name=test_name
                )

            session.add(test_music)
            session.commit()
            session.refresh(test_music)

        assert test_music.name == test_name
        assert test_music.id == 1
        assert test_music.description == None
        assert test_music.type == None
