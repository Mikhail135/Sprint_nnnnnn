from pages.main_page import MainPage
from pages.signup_page import SignupPage
import time
from url import Url

class TestAuthForm:
    def test_transition_to_authorization(self, driver):
        page = MainPage(driver)
        page.open_page()
        page.click_creat_acc()
        signup_page =SignupPage(driver)
        signup_page.input_reg_form()
        page.click_creat_acc()
        page.click_creat_acc_lower()
        time.sleep(2)
        log_in_to_the_website = signup_page.text_log_in_to_the_website()
        text_em = signup_page.text_email()
        text_pass = signup_page.text_password()
        assert log_in_to_the_website.is_displayed()
        assert text_pass.is_displayed()
        assert text_em.is_displayed()



