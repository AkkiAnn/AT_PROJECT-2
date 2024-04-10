import pytest
from selenium import webdriver

driver = None
driver_path = (r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")

# OrangeHRM URL
Ohrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture(scope="class")
def chrome_driver(request):

# Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Ohrm_url)
    request.cls.driver = Ohrm_url

    yield driver
# Teardown Chrome driver
    driver.quit()
