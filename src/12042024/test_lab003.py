from selenium import webdriver

# Selenium 4


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # Python Interpreter -> optimize if there is no command than I will stop the execution.