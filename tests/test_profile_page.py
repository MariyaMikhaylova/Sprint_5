from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


# переход по клику на «Конструктор»
def test_go_to_main_page_click_button_constructor(main_page, create_account, new_user):

    main_page.find_element(By.XPATH, locators.a_account).click()
    main_page.find_element(By.XPATH, locators.login_aut).send_keys(new_user.login)
    main_page.find_element(By.XPATH, locators.password_aut).send_keys(new_user.password)
    main_page.find_element(By.XPATH, locators.button_enter).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))

    main_page.find_element(By.XPATH, locators.a_account).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.a_profile)))

    main_page.find_element(By.XPATH, locators.button_constructor).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))
    assert "https://stellarburgers.nomoreparties.site/" == main_page.current_url

# переход по клику на логотип Stellar Burgers
def test_go_to_main_page_with_logo(main_page, create_account, new_user):

    main_page.find_element(By.XPATH, locators.a_account).click()
    main_page.find_element(By.XPATH, locators.login_aut).send_keys(new_user.login)
    main_page.find_element(By.XPATH, locators.password_aut).send_keys(new_user.password)
    main_page.find_element(By.XPATH, locators.button_enter).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))

    main_page.find_element(By.XPATH, locators.a_account).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.a_profile)))

    main_page.find_element(By.XPATH, locators.button_logo).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))
    assert "https://stellarburgers.nomoreparties.site/" == main_page.current_url

# выход по кнопке «Выйти» в личном кабинете
def test_logout_with_button_exit(main_page, create_account, new_user):

    main_page.find_element(By.XPATH, locators.a_account).click()
    main_page.find_element(By.XPATH, locators.login_aut).send_keys(new_user.login)
    main_page.find_element(By.XPATH, locators.password_aut).send_keys(new_user.password)
    main_page.find_element(By.XPATH, locators.button_enter).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.title)))

    main_page.find_element(By.XPATH, locators.a_account).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.a_profile)))

    main_page.find_element(By.XPATH, locators.button_exit).click()
    WebDriverWait(main_page, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_aut)))
    assert "https://stellarburgers.nomoreparties.site/login" == main_page.current_url
