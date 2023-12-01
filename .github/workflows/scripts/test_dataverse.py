import os
from urllib.parse import urljoin
import requests


class TestNativeAPI:
    def test_info(self):
        url = self.construct_url("api/info/version")
        response = requests.get(url)

        assert response.status_code == 200
        assert response.json()["status"] == "OK"

    def test_metadatablocks(self):
        url = self.construct_url("api/metadatablocks")
        response = requests.get(url)

        assert response.status_code == 200
        assert response.json()["status"] == "OK"

        expected = {
            "displayName": "Citation Metadata",
            "name": "citation",
        }

        assert any(
            {
                block["name"] == expected["name"]
                and block["displayName"] == expected["displayName"]
                for block in response.json()["data"]
            }
        )

    def test_create_collection(self):
        url = self.construct_url("api/dataverses/root")
        response = requests.post(
            url=url,
            headers=self.construct_header(),
            json={
                "name": "TestAction",
                "alias": "test_colleczion",
                "dataverseContacts": [
                    {"contactEmail": "burrito@burritoplace.yum"},
                ],
                "affiliation": "Burrito Research University",
                "description": "We do all the (burrito) science.",
                "dataverseType": "LABORATORY",
            },
        )

        assert response.status_code == 201
        assert response.json()["status"] == "OK"

    @staticmethod
    def construct_url(endpoint):
        BASE_URL = os.environ["BASE_URL"]
        return urljoin(BASE_URL, endpoint)

    @staticmethod
    def construct_header():
        return {"X-Dataverse-key": os.environ["API_TOKEN"]}
