from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import pytest
import time
import allure

@pytest.mark.smoke
@allure.title("Verify that an error message is displayed on Code Display when username is blank")
@allure.description("TC #1 - Simple test to validate error message when username is blank")
def test_cdpn_login():
    # Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(2)
    # Enter all the fields excepts the username
    driver.switch_to.frame(driver.find_element(By.ID, value="result"))
    email_element = driver.find_element(By.ID, value="email")
    pwd_element = driver.find_element(By.ID, value="password")
    cnf_pwd_element = driver.find_element(By.ID, value="password2")
    email_element.send_keys("admin@abc.com")
    pwd_element.send_keys("admin123")
    cnf_pwd_element.send_keys("admin123")
    submit_button = driver.find_element(By.XPATH, value='//*[@id="form"]/button')
    submit_button.click()
    time.sleep(5)
    # Verify that the error message comes when you click on the submit button. //*[@id="form"]/div[1]/small
    element_msg = driver.find_element(By.XPATH, value="//input[@id='username']/following::small")
    assert element_msg.text == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()


