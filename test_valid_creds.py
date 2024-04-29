import time  # for importing libraries for time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By # by is the class in selenium so for this imported By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def fixture_setup():  # after fixture what we will be writing will execute before testcase.
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here
    driver.get("http://127.0.0.1:8000/login/")  # hitting the url
    driver.maximize_window()  # for maximizing the window
    yield  # after yield what we will be writing will execute after testcase.
    driver.close()


def test_valid_creds(fixture_setup):
    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
    username.send_keys("najlashaujaat")

    password = driver.find_element(By.ID, "id_password")
    password.send_keys("Aa123456@@")

    view_password_button = driver.find_element(By.XPATH, "//button[@aria-label='Toggle Password Visibility']")
    view_password_button.click()

    remember_me_checkbox = driver.find_element(By.ID, "id_remember_me")
    if not remember_me_checkbox.is_selected():
        remember_me_checkbox.click()

    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    time.sleep(5)

    assert "Home Page" in driver.title  # Check if browser had name "cold chain or not" is present in the page title

