from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import pytest
import allure
import time


# Open the URL - https://www.idrive360.com/enterprise/login

driver = webdriver.Chrome()
driver.get("https://www.idrive360.com/enterprise/login")
driver.maximize_window()
# Enter the username, password - augtest_040823@idrive.com, 123456

element_user = driver.find_element(By.ID, value="username")
element_password = driver.find_element(By.ID, value="password")
element_user.send_keys("augtest_040823@idrive.com")
element_password.send_keys("123456")

submit_button = driver.find_element(By.ID, value="frm-btn")
submit_button.click()
time.sleep(30)


# Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trail end.
@pytest.mark.smoke
def test_url():
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error Message"
    msg_element = driver.find_element(By.CLASS_NAME, value="id-card-title")
    assert msg_element.text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()





=======
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import pytest
import allure
import time


# Open the URL - https://www.idrive360.com/enterprise/login

driver = webdriver.Chrome()
driver.get("https://www.idrive360.com/enterprise/login")
driver.maximize_window()
# Enter the username, password - augtest_040823@idrive.com, 123456

element_user = driver.find_element(By.ID, value="username")
element_password = driver.find_element(By.ID, value="password")
element_user.send_keys("augtest_040823@idrive.com")
element_password.send_keys("123456")

submit_button = driver.find_element(By.ID, value="frm-btn")
submit_button.click()
time.sleep(30)


# Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trail end.
@pytest.mark.smoke
def test_url():
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error Message"
    msg_element = driver.find_element(By.CLASS_NAME, value="id-card-title")
    assert msg_element.text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()

