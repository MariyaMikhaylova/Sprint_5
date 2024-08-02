from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# создание аккаунта для проверок авторизации
import conftest
login = conftest.generate_login(6)
password = conftest.generate_password(6)

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Mariia")
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()

driver.quit()

# вход по кнопке «Войти в аккаунт» на главной
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/main/section[2]/div/button").click()
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()

WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))
assert "https://stellarburgers.nomoreparties.site/" == driver.current_url
driver.quit()

# вход через кнопку «Личный кабинет»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))
assert "https://stellarburgers.nomoreparties.site/" == driver.current_url
driver.quit()

# вход через кнопку в форме регистрации
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, "html/body/div/div/main/div/div/p/a").click()
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))
assert "https://stellarburgers.nomoreparties.site/" == driver.current_url
driver.quit()

# вход через кнопку в форме восстановления пароля
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, "html/body/div/div/main/div/div/p[2]/a").click()
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()

WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/div/form/fieldset[2]")))
assert "https://stellarburgers.nomoreparties.site/reset-password" == driver.current_url
driver.quit()
