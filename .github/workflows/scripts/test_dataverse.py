import os
import requests


class TestNativeAPI:
    def test_info(self):
        # Test the native API
        r = requests.get("http://localhost:8080/api/info/version")
        assert r.status_code == 200
        assert r.json()["status"] == "OK"

    def test_metadatablocks(self):
        # Test the native API
        r = requests.get("http://localhost:8080/api/admin/metadatablocks")
        assert r.status_code == 200
        assert r.json()["status"] == "OK"

        expected = {
            "displayName": "Citation Metadata",
            "name": "citation",
        }

        assert any(
            {
                block["name"] == expected["name"]
                and block["displayName"] == expected["displayName"]
                for block in r.json()["data"]
            }
        )

    def test_create_collection(self):
        API_TOKEN = os.getenv("API_TOKEN")
        endpoint = "http://localhost:8080/api/dataverses/root"
        response = requests.post(
            endpoint,
            headers={"X-Dataverse-key": "7cd1f1e7-3838-4ea7-acb9-ab457990e9d8"},
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
