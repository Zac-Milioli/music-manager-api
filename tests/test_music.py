from conftest import client
from http import HTTPStatus
from datetime import datetime


class TestMusic:
    def test_return_list_database(self, client):
        response = client.get("/music")
        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.json(), list)

    def test_post_music(self, client):
        test_data = {
            "name": "testName",
            "description": "testDescription",
            "type": "testType",
        }
        date_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
        index = 1

        response = client.post("/music", json=test_data)

        test_data["created_at"] = date_now
        test_data["id"] = index
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == test_data

    def test_put_music_ok(self, client):
        test_data = {
            "name": "testName",
            "description": "testDescription",
            "type": "testType",
        }

        index = client.post("/music", json=test_data).json().get("id")

        test_new_data = {
            "name": "testNameNew",
            "description": "testDescriptionNew",
            "type": "testTypeNew",
        }
        response = client.put(f"/music/{index}", json=test_new_data)

        date_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
        test_new_data["created_at"] = date_now
        test_new_data["id"] = index

        assert response.status_code == HTTPStatus.OK
        assert response.json() == test_new_data

    def test_put_music_not_found(self, client):
        test_data = {
            "name": "testName",
            "description": "testDescription",
            "type": "testType",
        }
        client.post("/music", json=test_data)

        test_new_data = {
            "name": "testNameNew",
            "description": "testDescriptionNew",
            "type": "testTypeNew",
        }
        index = -1
        response = client.put(f"/music/{index}", json=test_new_data)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_delete_music_ok(self, client):
        test_data = {
            "name": "testName",
            "description": "testDescription",
            "type": "testType",
        }

        index = client.post("/music", json=test_data).json().get("id")

        date_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
        test_data["created_at"] = date_now
        test_data["id"] = index

        response = client.delete(f"/music/{index}")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == test_data

    def test_delete_music_not_found(self, client):
        index = -1
        response = client.delete(f"/music/{index}")

        assert response.status_code == HTTPStatus.NOT_FOUND
