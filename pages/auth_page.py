from selenium.webdriver.common.by import By
from .base_page import BasePage
from locator import Locator
import allure
from data import Data

class AuthPage(BasePage):
    @allure.step("нажатие кнопки Войти")
    def clc_button_enter(self):
        element = self.find_elements(Locator.ENTER_UP_BUTTON)
        return element

    @allure.step("ввести Электронная почта")
    def send_keys_email(self):
        element = self.find_elements(Locator.EMAIL_INPUT)
        element.send_keys(Data.email)

    @allure.step("ввести Пароль")
    def send_keys_password(self):
        element = self.find_elements(Locator.PASSWORD_INPUT)
        element.send_keys(Data.password)

    @allure.step("нажать Войти")
    def clc_button_enter(self):
        element = self.find_elements(Locator.LOGIN_BUTTON)
        element.click()

    @allure.step("появление кнопки Выйти")
    def wait_logout_button(self):
        self.wait_web_visibility(Locator.LOGOUT_BUTTON)

    @allure.step("появление текста Рецепты")
    def wait_text_recipes(self):
        self.wait_web_visibility(Locator.RECIPES_TEXT)

    @allure.step("поиск кнопки Выйти")
    def find_logout_button(self):
        element = self.find_elements(Locator.LOGOUT_BUTTON)
        return element

    @allure.step("поиск текста Рецепты")
    def find_text_recipes(self):
        element = self.find_elements(Locator.RECIPES_TEXT)
        return element

