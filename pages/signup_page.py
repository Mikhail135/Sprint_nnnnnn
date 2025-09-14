from selenium.webdriver.common.by import By
from .base_page import BasePage
from locator import Locator
from data import Data
import allure

class SignupPage(BasePage):
    @allure.step("Заполнение полей регистрации")
    def input_reg_form(self):
        self.find_elements(Locator.FIRST_NAME_INPUT).click()
        self.find_elements(Locator.FIRST_NAME_INPUT).send_keys(Data.first_name)
        self.find_elements(Locator.LAST_NAME_INPUT).click()
        self.find_elements(Locator.LAST_NAME_INPUT).send_keys(Data.last_name)
        self.find_elements(Locator.USER_NAME_INPUT).click()
        self.find_elements(Locator.USER_NAME_INPUT).send_keys(Data.user_name)
        self.find_elements(Locator.EMAIL_INPUT).click()
        self.find_elements(Locator.EMAIL_INPUT).send_keys(Data.email)
        self.find_elements(Locator.PASSWORD_INPUT).click()
        self.find_elements(Locator.PASSWORD_INPUT).send_keys(Data.password)

    @allure.step("Текст Войти на сайт")
    def text_log_in_to_the_website(self):
        element = self.find_elements(Locator.TEXT_LOG_IN_TO_THE_WEBSITE)
        return element

    @allure.step("Текст Электронная почта")
    def text_email(self):
        element = self.find_elements(Locator.TEXT_EMAIL)
        return element

    @allure.step("Текст Пароль")
    def text_password(self):
        element = self.find_elements(Locator.TEXT_PASSWORD)
        return element