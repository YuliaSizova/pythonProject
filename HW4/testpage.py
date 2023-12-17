from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml



class TestSearchLocators:
    ids = dict()
    with open(r"C:\Users\omen1\PycharmProjects\pythonProject\HW4\locators.yaml") as f:
        locators = yaml.safe_load(f)

    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    # for locator in locators["css"].keys():
    #     ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])




class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True


    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True


    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test form {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text


    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    #  функция ввода пароля
    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    # функция ввода названия поста в поле
    def enter_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_TITLE"], word, description="post title form")


    def enter_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word, description="post content form")


    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FIELD_YOUR_NAME"], word,
                                   description="enter your name form")


    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FIELD_YOUR_EMAIL"], word,
                                   description="enter your email form")


    def enter_content_to_form(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FIELD_CONTENT_TO_FORM"], word,
                                   description="enter content form in contact")


    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login button")


    def click_nwe_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_NEW_POST"], description="button create nwe post")


    def click_create_nwe_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="button self new post")


    def click_сontact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_CONTACT"], description="click to contact")


    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_CONTACT_US"], description="click button contact us")


    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error 401")


    def get_text_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RESULT_LOGIN"], description="result word- blog")


    def post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST"], description="result- title of the post")

    def result_switcying_to_form_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RESULT_SWITCHIHG_TO_FORM"],
                                          description="result - word -Contact us!")

    def get_alert_text(self):
        alert_field = self.driver.switch_to.alert
        text = alert_field.text
        logging.info(f"We find text {text} in alert")
        return text
