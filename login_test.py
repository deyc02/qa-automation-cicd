from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


URL = "https://practicetestautomation.com/practice-test-login/"
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()


# Test Case 1
# Accept valid username and password
def test_valid_login(driver):

    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.ID, "submit").click()

    heading = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.TAG_NAME,"h1"))
    )

    assert heading.text == "Logged In Successfully"


# Test Case 2
# Reject invalid credentials
def test_invalid_credentials(driver):

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()

    error = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.ID,"error"))
    )

    assert error.is_displayed()


# Test Case 3
# Display error message for invalid login attempts
def test_invalid_login_error_message(driver):

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("invalidPassword")
    driver.find_element(By.ID, "submit").click()

    error = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.ID,"error"))
    )

    assert "Your password is invalid!" in error.text


# Test Case 4
# Require username and password fields before submit
@pytest.mark.parametrize("username,password", [
    ("", ""),
    ("student", ""),
    ("", "Password123")
])

def test_required_fields(driver, username, password):

    if username:
        driver.find_element(By.ID, "username").send_keys(username)

    if password:
        driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "submit").click()

    current_url = driver.current_url

    # User should remain on login page
    assert "practice-test-login" in current_url


# Test Case 5
# Redirect user after successful login
def test_dashboard_redirect(driver):

    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.ID, "submit").click()

    WebDriverWait(driver,10).until(
        EC.url_contains("logged-in-successfully")
    )

    assert "logged-in-successfully" in driver.current_url