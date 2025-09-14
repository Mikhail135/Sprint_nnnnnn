
from pages.auth_page import AuthPage
from pages.create_recipe_page import CreateRecipePage


class TestCreateRecipe:
    def test_card_create_recipe(self, driver):
        auth_pg = AuthPage(driver)
        auth_pg.clc_button_enter()
        auth_pg.send_keys_email()
        auth_pg.send_keys_password()
        auth_pg.clc_button_enter()
        auth_pg.wait_logout_button()
        create_recipe = CreateRecipePage(driver)
        create_recipe.clc_button_create_recipe()
        create_recipe.send_recipe_name()
        create_recipe.send_name_ing()
        create_recipe.send_weight()
        create_recipe.clc_add_ingredient()
        create_recipe.send_time_cook()
        create_recipe.send_description()
        create_recipe.add_photo()
        create_recipe.click_create_recipe_button()


    def test_name_create_recipe(self, driver):
        auth_pg = AuthPage(driver)
        auth_pg.clc_button_enter()
        auth_pg.send_keys_email()
        auth_pg.send_keys_password()
        auth_pg.clc_button_enter()
        auth_pg.wait_logout_button()
        create_recipe = CreateRecipePage(driver)
        create_recipe.clc_button_create_recipe()
        create_recipe.send_recipe_name()
        create_recipe.send_name_ing()
        create_recipe.send_weight()
        create_recipe.clc_add_ingredient()
        create_recipe.send_time_cook()
        create_recipe.send_description()
        create_recipe.add_photo()
        create_recipe.click_create_recipe_button()