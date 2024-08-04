from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


# вход по кнопке «Войти в аккаунт» на главной
def test_authorization_from_main_page_header(main_page, create_account, new_user):

    main_page.find_element(By.XPATH, locators.button_enter_acc).click()
    main_page.find_element(By.XPATH, locators.login_aut).send_keys(new_user.login)
    main_page.find_element(By.XPATH, locators.password_aut).send_keys(new_user.password)
    main_page.find_element(By.XPATH, locators.button_enter).click()

    WebDriverWait(main_page, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))
    assert "https://stellarburgers.nomoreparties.site/" == main_page.current_url

# вход через кнопку «Личный кабинет»
def test_authorization_from_main_page_body(main_page, create_account, new_user):

    main_page.find_element(By.XPATH, locators.a_account).click()
    main_page.find_element(By.XPATH, locators.login_aut).send_keys(new_user.login)
    main_page.find_element(By.XPATH, locators.password_aut).send_keys(new_user.password)
    main_page.find_element(By.XPATH, locators.button_enter).click()

    WebDriverWait(main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))
    assert "https://stellarburgers.nomoreparties.site/" == main_page.current_url


# # вход через кнопку в форме регистрации
def test_authorization_from_registration_page(registration_page, create_account, new_user):

    registration_page.find_element(By.XPATH, locators.a_in).click()
    registration_page.find_element(By.XPATH, locators.login_aut).send_keys(new_user.login)
    registration_page.find_element(By.XPATH, locators.password_aut).send_keys(new_user.password)
    registration_page.find_element(By.XPATH, locators.button_enter).click()

    WebDriverWait(registration_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))
    assert "https://stellarburgers.nomoreparties.site/" == registration_page.current_url

# # вход через кнопку в форме восстановления пароля
def test_authorization_from_forgot_password_page(authorization_page, create_account, new_user):

    authorization_page.find_element(By.XPATH, locators.a_forgot_password).click()
    authorization_page.find_element(By.XPATH, locators.login_forgot).send_keys(new_user.login)
    authorization_page.find_element(By.XPATH, locators.button_restore).click()

    WebDriverWait(authorization_page, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.letter_code)))
    assert "https://stellarburgers.nomoreparties.site/reset-password" == authorization_page.current_url
