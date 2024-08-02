from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import conftest

# positive test
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Mariia")
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(conftest.generate_login(6))
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(conftest.generate_password(6))
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/div/div/p[2]")))
assert "https://stellarburgers.nomoreparties.site/login" == driver.current_url
driver.quit()

# negative test
# При некорректном пароле ошибка "Некорректный пароль"
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Mariia")
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(conftest.generate_login(6))
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(conftest.generate_password(3))
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()

assert driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[3]/div/p").text == "Некорректный пароль"
driver.quit()
