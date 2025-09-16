import allure
from locator import Locator
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Нажатие кнопки 'Создать аккаунт'")
    def click_creat_acc(self):
        self.find_elements(Locator.BUTTON_CREAT_ACCUNT).click()

    @allure.step("Нажатие кнопки в форме регистрации, снизу 'Создать аккаунт'")
    def click_creat_acc_lower(self):
        self.find_elements(Locator.BUTTON_CREAT_ACCUNT_LOWER).click()
