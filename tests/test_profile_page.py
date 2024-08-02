from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# создание аккаунта для проверок личного кабинета
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

# переход по клику на «Конструктор»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/div/nav/ul")))

driver.find_element(By.XPATH, "html/body/div/div/header/nav/ul/li[1]/a").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))
assert "https://stellarburgers.nomoreparties.site/" == driver.current_url
driver.quit()

# переход по клику на логотип Stellar Burgers
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/div/nav/ul")))

driver.find_element(By.XPATH, "html/body/div/div/header/nav/div/a").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))
assert "https://stellarburgers.nomoreparties.site/" == driver.current_url
driver.quit()

# выход по кнопке «Выйти» в личном кабинете
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(login)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "html/body/div/div/main/div/form/button").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/section/h1")))

driver.find_element(By.XPATH, "html/body/div/div/header/nav/a").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/div/nav/ul")))

driver.find_element(By.XPATH, "html/body/div/div/main/div/nav/ul/li[3]/button").click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html/body/div/div/main/div/div/p[2]")))
assert "https://stellarburgers.nomoreparties.site/login" == driver.current_url
driver.quit()
