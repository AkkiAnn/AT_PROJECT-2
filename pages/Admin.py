from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Admin_window:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    admin_x = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]'

    def click_admin(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(By.XPATH, self.admin_x)).click()

    def is_clear(self, value):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(value))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def topbar_menu(self):

        valid_head = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(By.XPATH, "//div[contains(@class, 'oxd-topbar-body')]"))
        print(len(valid_head))

        # Find all <span> Tag
        span_tag = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(By.TAG_NAME, 'span'))

        # Define the class name you're looking for
        define_class = "oxd-topbar-body-nav-tab-item"

        # Iterate over each <span> element
        for span in span_tag:
            # Check if the span has the desired class
            if define_class in span.get_attribute("class"):
                # Get the text inside the span
                text = span.text
                print(text)

    def sidebar_menu(self):

        side_menu = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(By.XPATH, "//div[contains(@class, 'oxd-topbar-body')]"))
        print(len(side_menu))

    # Find all <span> Tag
        span_tag = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(By.TAG_NAME, 'span'))

        # Define the class name you're looking for
        define_class = "oxd-text oxd-text--span oxd-main-menu-item--name"

    # Iterate over each <span> element
        for span in span_tag:
            # Check if the span has the desired class
            if define_class in span.get_attribute("class"):
                # Get the text inside the span
                text = span.text
                print(text)
