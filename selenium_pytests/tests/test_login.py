import pytest
from selenium import webdriver
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium_pytests.selenium_tests.login_page import LoginPage
from selenium_pytests.utils.config import load_config

config = load_config()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password, expected_result", [("standard_user", "secret_sauce", "Products"),
                                                                 ("invalid_user", "wrong_password", "Epic error")])
def test_login(driver, username, password, expected_result):
    driver.get(config["base_url"])

    login_page = LoginPage(driver)

    login_page.set_username(username)
    login_page.set_password(password)
    login_page.click_login()

    if expected_result == "Products":
        assert login_page.get_title() == expected_result
    else:
        assert login_page.get_error_message().startswith(expected_result)