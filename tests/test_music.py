"""Classes e funções referentes aos testes unitários da API de Music"""

from http import HTTPStatus
from datetime import datetime
from src.models.music_model import Music
from src.schemas.music_schema import MusicPublic, MusicSchema

class TestMusic:
    "Classe e testes para a API"

    def test_get_music(self, client):
        "Testa o retorno vazio da base de dados"
        response = client.get("/music")
        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.json(), list)

    def test_get_music_created(self, client, music: Music):
        "Testa o retorno da base de dados com 1 registro"
        music = MusicPublic.model_validate(music).model_dump()

        response = client.get("/music").json()
        response[0]["created_at"] = datetime.fromisoformat(response[0]["created_at"])

        assert response[0] == music

    def test_post_music(self, client):
        "Testa a criação de uma Music"
        test_data = {
            "name": "testName",
            "description": "testDescription",
            "type": "testType",
        }
        response = client.post("/music", json=test_data)

        assert response.status_code == HTTPStatus.CREATED
        assert response.json()["name"] == test_data["name"]

    def test_post_music_conflict(self, client, music: Music):
        "Testa a criação de uma Music que já existe"
        music = MusicSchema.model_validate(music).model_dump()
        response = client.post("/music", json=music)

        assert response.status_code == HTTPStatus.CONFLICT

    def test_put_music_ok(self, client, music: Music):
        "Testa a alteração de uma Music"
        music = MusicPublic.model_validate(music)
        music.name = "testNameNew"

        music_schema = MusicSchema(
            name=music.name, description=music.description, type=music.type
        ).model_dump()

        response = client.put(f"/music/{music.id}", json=music_schema)
        response_json = response.json()
        response_json["created_at"] = datetime.fromisoformat(response_json["created_at"])

        assert response.status_code == HTTPStatus.OK
        assert response_json == music.model_dump()

    def test_put_music_not_found(self, client):
        "Testa o erro da alteração de uma Music"
        test_new_data = {
            "name": "testName",
            "description": "testDescription",
            "type": "testType",
        }
        index = -1
        response = client.put(f"/music/{index}", json=test_new_data)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_delete_music_ok(self, client, music: Music):
        "Testa a exclusão de uma Music"
        music = MusicPublic.model_validate(music)
        response = client.delete(f"/music/{music.id}")
        response_json = response.json()
        response_json["created_at"] = datetime.fromisoformat(response_json["created_at"])

        assert response.status_code == HTTPStatus.OK
        assert response_json == music.model_dump()

    def test_delete_music_not_found(self, client):
        "Testa a falha da exclusão de uma Music"
        index = -1
        response = client.delete(f"/music/{index}")

        assert response.status_code == HTTPStatus.NOT_FOUND
