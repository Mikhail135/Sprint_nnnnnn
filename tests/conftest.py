from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import pytest
from url import Url

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.site)
    yield driver
    driver.quit()