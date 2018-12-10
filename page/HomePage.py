#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Lillian Zhou"

"""#this Base class is serving basic attributes for every single page inherited from Page class
"""
import allure
from locator.HomePageLocator import HomePageLocator
from page.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = HomePageLocator
        super().__init__(driver)

    def check_result_is_loaded(self):
        self.get_element_by_xpath(self.locator.SEARCH_RESULT)

    def check_search_button(self, search_value):
        with allure.step('set search value'):
            self.set_element(self.locator.SEARCH_INPUT, search_value)
        with allure.step('click search button'):
            self.click_element_by_xpath(self.locator.SEARCH_BUTTON)
        with allure.step('check search result is loaded'):
            self.check_result_is_loaded()

    def check_search_directly(self, search_value):
        with allure.step('set search value'):
            self.set_element(self.locator.SEARCH_INPUT, search_value)
        with allure.step('click search button'):
            self.click_element_by_xpath(self.locator.SEARCH_DIRECTLY_BUTTON)
