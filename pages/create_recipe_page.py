from pathlib import Path
from .base_page import BasePage
from locator import Locator
import allure
from data import Data

class CreateRecipePage(BasePage):
    @allure.step("нажатие кнопки Создать рецепт")
    def clc_button_create_recipe(self):
        element = self.find_elements(Locator.CREATE_RECIPE)
        element.click()

    @allure.step("заполнение Название рецепта")
    def send_recipe_name(self):
        element = self.find_elements(Locator.RECIPE_NAME)
        element.send_keys(Data.recipe_name)

    @allure.step("нажатие кнопки Создать рецепт")
    def clc_button_create_recipe(self):
        element = self.find_elements(Locator.CREATE_RECIPE)
        element.click()

    @allure.step("заполнение название игредиента")
    def send_name_ing(self):
        element = self.find_elements(Locator.INGREDIENT)
        element.send_keys(Data.eel[:2])
        element = self.wait_web_visibility(Locator.INGREDIENT_EEL)
        element.click()

    @allure.step("заполнение веса игредиента")
    def send_weight(self):
        element = self.find_elements(Locator.WEIGHT_INPUT)
        element.send_keys(Data.weight)

    @allure.step("нажать Добавить ингредиент")
    def clc_add_ingredient(self):
        element = self.wait_web_clickable(Locator.ADD_INGREDIENT)
        element.click()

    @allure.step("заполнение Время приготовления")
    def send_time_cook(self):
        element = self.find_elements(Locator.TIME_COOK)
        element.send_keys(Data.time_cook)

    @allure.step("заполнение Описание рецепта")
    def send_description(self):
        element = self.find_elements(Locator.DESCRIPTION)
        element.send_keys(Data.recipe_name)

    @allure.step("Добавлеине фото")
    def add_photo(self):
        APP_DIR = Path(__file__).parent.parent
        image_path = APP_DIR / "resources" / "яблоки.jpg"
        file_input = self.find_elements(Locator.ADD_PHOTO)
        file_input.send_keys(str(image_path))

    @allure.step("нажать Создать рецепт")
    def click_create_recipe_button(self):
        element = self.find_elements(Locator.CREATE_RECIPE_BUTTON)
        element.click()