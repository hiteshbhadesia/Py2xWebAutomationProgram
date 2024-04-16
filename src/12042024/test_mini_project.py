from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

driver = webdriver.Chrome()
# open the url
driver.get("https://katalon-demo-cura.herokuapp.com/")

# click on the make appointment button
appoint_button = driver.find_element(by=By.ID, value="btn-make-appointment")
appoint_button.click()

# verify that url changes - assert
# print(driver.title)
assert driver.title == "CURA Healthcare Service"
time.sleep(3)

# enter the username, password
user_id = driver.find_element(By.ID, value='txt-username')
user_pwd = driver.find_element(By.ID, value="txt-password")
user_id.send_keys("John Doe")
user_pwd.send_keys("ThisIsNotAPassword")

login_button = driver.find_element(By.ID, value="btn-login")
login_button.click()


# next page verify the current url
@pytest.mark.smoke
def test_current_url():
    current_url = driver.current_url
    print(driver.title)
    assert driver.title == "CURA Healthcare Service"


# make appointment text on the web page.
def test_url_text():
    text_element = driver.find_element(By.XPATH, value="//div/h2")
    assert text_element.text == "Make Appointment"
    time.sleep(3)
