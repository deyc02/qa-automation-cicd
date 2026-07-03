def test_valid_login():

    driver = setup_driver()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    assert "Logged In Successfully" in driver.title

    driver.quit()


# TC_LOGIN_002 - Invalid Password
def test_invalid_password():

    driver = setup_driver()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("WrongPassword")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    error = driver.find_element(By.ID, "error").text

    assert "Your password is invalid!" in error

    driver.quit()


# TC_LOGIN_003 - Invalid Username
def test_invalid_username():

    driver = setup_driver()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    error = driver.find_element(By.ID, "error").text

    assert "Your username is invalid!" in error

    driver.quit()


# TC_LOGIN_004 - Blank Username
def test_blank_username():

    driver = setup_driver()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    current_url = driver.current_url

    assert "practice-test-login" in current_url

    driver.quit()


# TC_LOGIN_005 - Blank Password
def test_blank_password():

    driver = setup_driver()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    current_url = driver.current_url

    assert "practice-test-login" in current_url

    driver.quit()


# TC_LOGIN_006 - Blank Username and Password
def test_blank_credentials():

    driver = setup_driver()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    current_url = driver.current_url

    assert "practice-test-login" in current_url

    driver.quit()


# TC_LOGIN_007 - Logout
def test_logout():

    driver = setup_driver()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    driver.find_element(By.LINK_TEXT, "Log out").click()

    time.sleep(2)

    assert "Test Login" in driver.title

    driver.quit()