from testpage import OperationsHelper
import logging
import yaml
import time
import requests
from conftest import auth_token
import pytest

with open(r"C:\Users\omen1\PycharmProjects\pythonProject\HW4\testdata.yaml") as f:
    testdata = yaml.safe_load(f)

with open(r'C:\Users\omen1\PycharmProjects\pythonProject\HW4\config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
    logging.info("Test1 finished")


def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.get_text_blog() == "Blog"
    logging.info("Test2 finished")


def test_step3(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser, testdata['address'])

    # создания поста
    testpage.click_nwe_post_button()
    testpage.enter_title_post("new title")
    testpage.enter_content_post("content")
    testpage.click_create_nwe_post_button()

    time.sleep(3)

    # Проверка наличия названия поста на странице
    assert testpage.post() == "new title"
    logging.info("Test3 finished")


def test_step4(browser):
    logging.info("Test4 starting")
    testpage = OperationsHelper(browser, testdata['address'])

    testpage.click_сontact_button()
    time.sleep(2)
    assert testpage.result_switcying_to_form_text() == "Contact us!"
    logging.info("Test4 finished")


def test_step5(browser):
    logging.info("Test5 starting")
    testpage = OperationsHelper(browser, testdata['address'])

    testpage.enter_name("name")
    testpage.enter_email("email@email.ru")
    testpage.enter_content_to_form("content")
    testpage.click_contact_us_button()

    time.sleep(3)

    assert testpage.get_alert_text() == "Form successfully submitted"
    logging.info("Test5 finished")


def test_api_check_post_title(auth_token, send_email):
    try:
        logging.info("Test6 API starting")
        res_get = requests.get(url=data['url2'], headers={"X-Auth-Token": auth_token}, params={"owner": "notMe"})
        res_json = res_get.json()
        assert res_get.status_code == 200
        assert 'data' in res_json

        post_titles = [post["title"] for post in res_json["data"]]
        assert data["title"] in post_titles
        logging.info("Test6 finished")


    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
