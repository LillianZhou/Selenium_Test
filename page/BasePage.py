#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Lillian Zhou"

"""#this Base class is serving basic attributes for every single page inherited from Page class
"""
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,WebDriverException
import allure
from allure_commons.types import AttachmentType
from time import sleep
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element_by_xpath(self, locator, timeout=100):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator)))
        return element

    def set_element(self, locator, value):
        element = self.get_element_by_xpath(locator)
        element.clear()
        element.send_keys(value)

    def catch_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), \
                      attachment_type=AttachmentType.PNG)

    def click_element_by_xpath(self, locator, timeout=100):
        try:
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, locator)))
            sleep(2)
            button.click()
        except WebDriverException:
            self.catch_screenshot()
            assert False, 'Click button {0} Failed '.format(locator)



