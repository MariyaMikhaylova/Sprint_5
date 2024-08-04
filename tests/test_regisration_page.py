from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import helpers
import locators

# positive test
# успешная регистрация пользователя
def test_get_new_user_true(registration_page, new_user):

    registration_page.find_element(By.XPATH, locators.name).send_keys("Mariia")
    registration_page.find_element(By.XPATH, locators.login).send_keys(new_user.login)
    registration_page.find_element(By.XPATH, locators.password).send_keys(new_user.password)
    registration_page.find_element(By.XPATH, locators.button_register).click()

    WebDriverWait(registration_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.button_enter)))
    assert "https://stellarburgers.nomoreparties.site/login" == registration_page.current_url

# negative test
# При некорректном пароле ошибка "Некорректный пароль"
def test_short_password_error_text(registration_page):

    registration_page.find_element(By.XPATH, locators.name).send_keys("Mariia")
    registration_page.find_element(By.XPATH, locators.login).send_keys(helpers.generate_login(6))
    registration_page.find_element(By.XPATH, locators.password).send_keys(helpers.generate_password(3))
    registration_page.find_element(By.XPATH, locators.button_register).click()

    assert registration_page.find_element(By.CLASS_NAME, locators.password_error).text == "Некорректный пароль"
