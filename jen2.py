import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.integration
@pytest.mark.smoke
def test_001_lambdatest_ajax_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
    driver.find_element(By.ID, "title").send_keys("Pytest Tutorial")
    driver.find_element(By.ID, "description").send_keys("LambdaTest Selenium Playground")
    driver.find_element(By.ID, "btn-submit").click()
    request = driver.find_element(By.ID, "submit-control").text
    assert "Processing" in request

def test_002_e2e():
    print("End To End Test")

@pytest.mark.smoke
def test_003_login():
    print("Log Into Application")

@pytest.mark.smoke
def test_004_logout():
    print("Log Out Application")
