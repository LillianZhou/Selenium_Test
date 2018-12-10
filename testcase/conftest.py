from selenium import webdriver
import pytest
import allure
from data.data_log_in import CHROME_DRIVER, FIREFOX_DRIVER, URL


@pytest.fixture(scope="module")
def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,options=options)
    return driver


@pytest.fixture(scope="module")
def home_page(get_chrome_driver, request):
    driver = get_chrome_driver
    driver.get(URL)

    def quit_driver():
        driver.quit()
    request.addfinalizer(quit_driver)
    return driver
