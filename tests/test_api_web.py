import pytest
import requests
import json


class TestWebApi:

    @pytest.mark.seo
    def test_mock_service(self):
        url = 'https://exist.ua'
        s = requests.Session()
        r = s.get(url)
        #resp = requests.get(url)
        #assert resp.status_code == 200
        # assert resp.json()["code"] == 1
        print(r.headers)