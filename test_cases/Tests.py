import pytest
from pages.Password_reset import Reset_pass
from pages.Login import Login
from pages.Admin import Admin_window

# Datas for Testcase validation.
reset_pwd_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset'
Admin_Title = 'OrangeHRM'
admin_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
username = "Admin"
password = "admin123"

@pytest.mark.usefixtures("chrome_driver")
class Test_update:

    # Test Case_PIM_01
    def test_reset_password(self):

        try:
            reset = Reset_pass(self.driver)
            reset.reset_password(self.username)


            #  Verify the current URL with the reset password page URL.
            exp_url = reset.is_clear(self.reset_pwd_url)
            assert self.current_url == exp_url, "go and check the TC_PIM_01"
            print("Reset Password link sent successfully")

        except Exception as e:
            print("something went wrong in test_reset_password is ", e)


    # Test Case_PIM_02
    def test_validate_header(self):

        try:
            # Entering the Login.
            login = Login(self.driver)
            login.log_in(self.username, self.password)

            # Click the Admin Module.
            admin = Admin_window(self.driver)
            display_headers = admin.click_admin()

            # Validate the Title.
            exp_title = admin.get_title(self.Admin_Title)
            assert self.current_title == exp_title, "go and check validate the title in TC_PIM_02"
            print("got the title of OrangeHRM is performed successfully")

            # Validate the Header Texts.
            admin.topbar_menu()

            # Verify the current URL with the Admin URL.
            display_headers.is_displayed()
            assert self.current_url == self.admin_url, "go and check the TC_PIM_02"
            print("Admin Page Header successfully displayed")

        except Exception as e:
            print("something went wrong in test_validate_header", e)


# Test Case_PIM_03
    def test_validate_side_menu(self):

        try:
            # Entering the Login.
            login = Login(self.driver)
            login.log_in(self.username, self.password)

            # Click the Admin Module.
            admin = Admin_window(self.driver)
            display_side_menu = admin.click_admin()

            # Validate the Side-Menu Texts.
            admin.sidebar_menu()

            # Verify the current URL with the Admin URL.
            display_side_menu.is_displayed()
            assert self.current_url == self.admin_url, "go and check the TC_PIM_03"
            print("Admin Page side-menu successfully displayed")

        except Exception as e:
            print("something went wrong in test_validate_side_menu", e)
