import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from url import Url

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=chrome_options
    )

    driver.get(Url.site)
    yield driver
    driver.quit()