from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class Reset_pass:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # Locators of Reset Password page.
    forgot_pass_lt = 'Forgot your password? '
    reset_u_n = 'username'
    reset_pwd_btn_lt = ' Reset Password '

    # Method for Reset Password.
    def reset_password(self, username):

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(By.LINK_TEXT, self.forgot_pass_lt)).click()
        driver.implicitly_wait(20)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(By.NAME, self.reset_u_n)).send_keys(username)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, self.reset_pwd_btn_lt)).click()

        driver.implicitly_wait(20)
        return self.do_login()