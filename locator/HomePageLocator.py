#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Lillian Zhou"

"""There are all xpath locators for the home page 
"""


class HomePageLocator(object):

    SEARCH_INPUT = "//input[@name='q']"
    SEARCH_BUTTON = "//input[@name='btnK']"
    SEARCH_DIRECTLY_BUTTON = "//input[@name='btnI']"
    SEARCH_RESULT = "//div[@id='resultStats']"
