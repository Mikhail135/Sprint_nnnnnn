import allure

from locator import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Нажатие кнопки 'Создать аккаунт'")
    def click_creat_acc(self):
        self.find_elements(Locator.BUTTON_CREAT_ACCUNT).click()

    @allure.step("Нажатие кнопки в форме регистрации, снизу 'Создать аккаунт'")
    def click_creat_acc_lower(self):
        self.find_elements(Locator.BUTTON_CREAT_ACCUNT_LOWER).click()