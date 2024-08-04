from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


# переход по клику на «Личный кабинет»
def test_go_to_authorization_page(main_page):

    main_page.find_element(By.XPATH, locators.a_account).click()
    WebDriverWait(main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_aut)))
    assert "https://stellarburgers.nomoreparties.site/login" == main_page.current_url

# переход к разделy «Булки»
def test_go_to_chapter_buns(main_page):

    main_page.find_element(By.XPATH, locators.chapter_sauces).click()
    main_page.find_element(By.XPATH, locators.chapter_buns).click()
    assert "tab_tab_type_current__2BEPc" in main_page.find_element(By.XPATH, locators.chapter_buns).get_attribute("class")

# переход к разделy «Соусы»
def test_go_to_chapter_sauces(main_page):

    main_page.find_element(By.XPATH, locators.chapter_sauces).click()
    assert "tab_tab_type_current__2BEPc" in main_page.find_element(By.XPATH, locators.chapter_sauces).get_attribute("class")

# переход к разделy «Начинки»
def test_go_to_chapter_fillings(main_page):

    main_page.find_element(By.XPATH, locators.chapter_fillings).click()
    assert "tab_tab_type_current__2BEPc" in main_page.find_element(By.XPATH, locators.chapter_fillings).get_attribute("class")
