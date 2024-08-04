import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import helpers
import locators


# создание аккаунта
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

@pytest.fixture(scope='function')
def create_account(registration_page, new_user):
    registration_page.find_element(By.XPATH, locators.name).send_keys("Mariia")
    registration_page.find_element(By.XPATH, locators.login).send_keys(new_user.login)
    registration_page.find_element(By.XPATH, locators.password).send_keys(new_user.password)
    registration_page.find_element(By.XPATH, locators.button_register).click()

@pytest.fixture(scope='function')
def new_user():
    user = User(helpers.generate_login(6), helpers.generate_password(6))
    return user


# страница регистрации
@pytest.fixture(scope='function')
def registration_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver
    driver.quit()

# главная страница
@pytest.fixture(scope='function')
def main_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

# страница авторизации
@pytest.fixture(scope='function')
def authorization_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    yield driver
    driver.quit()
