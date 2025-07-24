import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium_pytests.selenium_tests.login_page import LoginPage
from selenium_pytests.utils.config import load_config
from selenium import webdriver

config = load_config()


@pytest.fixture
def driver(request):
    browser = request.param
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Navegador no soportado: {browser}")

    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("driver, username, password, expected_result", [
    ("chrome", config["valid_user"], config["valid_password"], "Products"),
    ("firefox", config["valid_user"], config["valid_password"], "Products"),
], indirect=["driver"])
def test_login(driver, username, password, expected_result):
    driver.get(config["base_url"])
    login_page = LoginPage(driver)
    login_page.set_username(username)
    login_page.set_password(password)
    login_page.click_login()
    assert login_page.get_title() == expected_result, f"Esperado: {expected_result}"

