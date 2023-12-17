import logging
import requests
import yaml
from conftest import auth_token
import pytest

with open(r'C:\Users\omen1\PycharmProjects\pythonProject\HW4\config.yaml') as f:
    data = yaml.safe_load(f)


def test_check_post_title(auth_token, send_email):
    try:
        logging.info("Test6 API starting")
        res_get = requests.get(url=data['url2'], headers={"X-Auth-Token": auth_token}, params={"owner": "notMe"})
        res_json = res_get.json()
        assert res_get.status_code == 200
        assert 'data' in res_json

        post_titles = [post["title"] for post in res_json["data"]]
        assert data["title"] in post_titles
        logging.info("Test6 finished")

    except:
        logging.exception(f"API request failed")
        logging.error("API request failed")


