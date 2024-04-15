from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome() # Create the Session - POST Request
    driver.get("https://app.vmo.com") # GET request to URL param
    print(driver.title)
    assert driver.title == "Login - VMO"
    time.sleep(5)
