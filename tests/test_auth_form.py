from pages.main_page import MainPage
from pages.signup_page import SignupPage
import time

class TestAuthForm:
    def test_transition_to_authorization(self, driver):
        page = MainPage(driver)
        page.click_creat_acc()
        signup_page =SignupPage(driver)
        signup_page.input_reg_form()
        page.click_creat_acc()
        page.click_creat_acc_lower()
        time.sleep(2)
        log_in_to_the_website = signup_page.text_log_in_to_the_website()
        assert log_in_to_the_website.is_displayed()

    def test_auth_form(self, driver):
        page = MainPage(driver)
        page.click_creat_acc()
        signup_page =SignupPage(driver)
        signup_page.input_reg_form()
        page.click_creat_acc()
        page.click_creat_acc_lower()
        text_em = signup_page.text_email()
        text_pass = signup_page.text_password()
        assert text_pass.is_displayed()
        assert text_em.is_displayed()

