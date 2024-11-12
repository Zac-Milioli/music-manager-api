from conftest import client
from http import HTTPStatus
from datetime import datetime

class TestMusic:
    def test_return_list_database(self, client):
        response = client.get("/music")
        assert response.status_code == HTTPStatus.OK

    def test_post_music(self, client):
        test_data = {
                "name": "testName",
                "description": "testDescription",
                "type": "testType"
            }
        date_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
        index = 1
        
        response = client.post("/music", json=test_data)

        test_data['date'] = date_now
        test_data['id'] = index
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == test_data