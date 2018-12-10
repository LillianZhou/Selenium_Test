import pytest
import allure
from page.HomePage import HomePage


class TestHomePage(object):

    @pytest.mark.parametrize("search_value", ['python', 'pytest'])
    def test_search_button(self, home_page, search_value):
        driver = home_page
        page = HomePage(driver)
        page.check_search_button(search_value)
        driver.back()

    @pytest.mark.parametrize("search_value", ['selenium', 'allure'])
    def test_search_directly_button(self, home_page, search_value):
        driver = home_page
        page = HomePage(driver)
        page.check_search_directly(search_value)
        driver.back()
