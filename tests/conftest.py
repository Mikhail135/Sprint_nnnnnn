import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    selenoid_url = os.getenv("SELENOID_URL", "http://selenoid:4444/wd/hub")
    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )
    yield driver
    driver.quit()
