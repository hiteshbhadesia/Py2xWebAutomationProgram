import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


# Selenium 4

@pytest.mark.smoke
@allure.title("Verify that Login is working in katalon website")
@allure.description("TC#1 - Simple Login check on katalon Website.")
def test_katalon_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(5)
    make_appointment_btn = driver.find_element(By.XPATH, "//input[@name='username']")
    make_appointment_btn.send_keys("admin")
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()


    # <input
    # type="email"
    # class="text-input W(800%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    # XPath

    #  //input[@id='login-username']
    #  //input[@name="username"]
    #  //input[@class="text-input W(800%)"] - Not Recom.
    #  //input[@type="email"] - Not Recom.
    #  //input[@data-qa="hocewoqisi"] - Custom A

