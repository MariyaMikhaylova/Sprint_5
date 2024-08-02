from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# переход по клику на «Личный кабинет»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/div/form/fieldset[1]")))
assert "https://stellarburgers.nomoreparties.site/login" == driver.current_url
driver.quit()

# переход к разделy «Булки»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/main/section/div/div[2]").click()
driver.find_element(By.XPATH, "html/body/div/div/main/section/div/div[1]").click()

assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "html/body/div/div/main/section/div/div[1]").get_attribute("class")
driver.quit()

# переход к разделy «Соусы»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/main/section/div/div[2]").click()

assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "html/body/div/div/main/section/div/div[2]").get_attribute("class")
driver.quit()

# переход к разделy «Начинки»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/main/section/div/div[3]").click()

assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "html/body/div/div/main/section/div/div[3]").get_attribute("class")
driver.quit()
