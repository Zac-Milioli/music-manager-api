"""Classes e funções referentes aos testes unitários da API de Music"""

from http import HTTPStatus
from datetime import datetime
from src.schemas.music_schema import MusicPublic

class TestMusic:
    "Classe e testes para a API"

    def test_get_music(self, client):
        "Testa o retorno vazio da base de dados"
        response = client.get("/music")
        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.json(), list)

    def test_get_music_created(self, client, music: MusicPublic):
        "Testa o retorno da base de dados com 1 registro"
        response = client.get("/music")
        assert response.json()[0].get("name") == music.name

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

    def test_post_music_conflict(self, client, music: MusicPublic):
        "Testa a criação de uma Music que já existe"
        response = client.post("/music", json={"name": music.name})

        assert response.status_code == HTTPStatus.CONFLICT

    def test_put_music_ok(self, client, music: MusicPublic):
        "Testa a alteração de uma Music"
        music.name = "testNameNew"
        response = client.put(f"/music/{music.id}", json={"name": music.name})

        assert response.status_code == HTTPStatus.OK
        assert response.json()["name"] == music.name

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

    def test_delete_music_ok(self, client, music: MusicPublic):
        "Testa a exclusão de uma Music"
        response = client.delete(f"/music/{music.id}")

        assert response.status_code == HTTPStatus.OK
        assert response.json()["name"] == music.name

    def test_delete_music_not_found(self, client):
        "Testa a falha da exclusão de uma Music"
        index = -1
        response = client.delete(f"/music/{index}")

        assert response.status_code == HTTPStatus.NOT_FOUND
