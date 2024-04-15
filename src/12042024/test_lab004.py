from selenium import webdriver
import time

def test_open_vwologin():
    driver = webdriver.Chrome() # Create the Session - POST Request
    driver.get("https://app.vmo.com") # GET request to URL param
    time.sleep(5)
