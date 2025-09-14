from selenium.webdriver.common.by import By
from data import Data

class Locator:
    BUTTON_CREAT_ACCUNT = (By.XPATH, "//*[contains(@class, 'style_link__1kPh8') and contains(text(), 'Создать аккаунт')]")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='last_name']")
    USER_NAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_CREAT_ACCUNT_LOWER = (By.XPATH, "//form//button[contains(text(), 'Создать аккаунт')]")
    TEXT_LOG_IN_TO_THE_WEBSITE = (By.XPATH, "//h1[contains(text(), 'Войти на сайт')]")
    TEXT_EMAIL = (By.XPATH, "//*[contains(@class, 'styles_inputLabelText__WsyhD') and contains(text(), 'Пароль')]")
    TEXT_PASSWORD = (By.XPATH, "//*[contains(@class, 'styles_inputLabelText__WsyhD') and contains(text(), 'Электронная почта')]")
    ENTER_UP_BUTTON = (By.XPATH, "//a[normalize-space(text())='Войти']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space(text())='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space(text())='Выход']")
    RECIPES_TEXT = (By.XPATH, "//h1[normalize-space(text())='Рецепты']")
    CREATE_RECIPE = (By.XPATH, "//a[normalize-space(text())='Создать рецепт']")
    RECIPE_NAME = (By.XPATH, "(//input[@class='styles_inputField__3eqTj'])[1]")
    INGREDIENT = (By.CSS_SELECTOR, ".styles_ingredientsInput__1zzql")
    INGREDIENT_EEL = (By.XPATH, f"//div[text()='{Data.eel}']")
    WEIGHT_INPUT = (By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT")
    ADD_INGREDIENT = (By.CLASS_NAME, "styles_ingredientAdd__3fc32")
    TIME_COOK = (By.XPATH, "(//input[@class='styles_inputField__3eqTj'])[2]")
    DESCRIPTION = (By.CLASS_NAME, "styles_textareaField__1wfhC")
    ADD_PHOTO = (By.CSS_SELECTOR, "input.styles_fileInput__3HjP3")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")









