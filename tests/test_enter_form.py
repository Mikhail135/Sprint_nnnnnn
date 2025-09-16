from pages.auth_page import AuthPage

class TestAuthForm:
    def test_log_out__button(self, driver):
        auth_pg = AuthPage(driver)
        auth_pg.open_page()
        auth_pg.clc_button_enter()
        auth_pg.send_keys_email()
        auth_pg.send_keys_password()
        auth_pg.clc_button_enter()
        auth_pg.wait_logout_button()
        element = auth_pg.find_logout_button()
        assert element.is_displayed()


    def test_main_page(self, driver):
        auth_pg = AuthPage(driver)
        auth_pg.open_page()
        auth_pg.clc_button_enter()
        auth_pg.send_keys_email()
        auth_pg.send_keys_password()
        auth_pg.clc_button_enter()
        auth_pg.wait_text_recipes()
        element = auth_pg.find_text_recipes()
        assert element.is_displayed()