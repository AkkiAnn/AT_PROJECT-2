from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Login:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # Locators of Login Page.
    l_username_n = 'username'
    l_password_n = 'password'
    login_btn_x = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    # Login function to enter the Web page.
    def log_in(self, username, password):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, self.l_username_n)).send_keys(username)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, self.l_password_n)).send_keys(password)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, self.login_btn_x)).click()

        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present()).accept()

        except Exception as e:
            print(" Error in login ", e)
