from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find
from webium.controls.link import Link

__author__ = 'g_trofimov'


class CGNCommonPage(BasePage):
    navigation_panel = Find(WebElement, By.CLASS_NAME, 'nav navbar-nav')
    """@type : WebElement"""

    home_button = Find(Link, By.XPATH, './/a[@class="btn btn-default"]/i[@class="glyphicon glyphicon-home"]')
    """@type : Link"""

    instrument_panel = Find(WebElement, By.CLASS_NAME, 'nav navbar-nav navbar-right')
    """@type : WebElement"""

    def is_navigation_panel_present(self):
        return self.is_element_present('navigation_panel')

    def is_home_button_present(self):
        if self.is_navigation_panel_present():
            return self.is_element_present('home_button')

    def is_instrument_panel_present(self):
        return self.is_element_present('instrument_panel')

    def open_home_page(self):
        if self.is_home_button_present():
            self.home_button.click()
