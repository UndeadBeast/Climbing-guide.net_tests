# -*- coding: utf-8 -*-
from my_config import my_config
from webium.controls.link import Link
from pages.common_page import CGNCommonPage
from selenium.webdriver.common.by import By
from webium.find import Find
from selenium.webdriver.remote.webelement import WebElement

__author__ = 'g_trofimov'


class CGNHomePage(CGNCommonPage):
    page_locator = Find(Link, By.LINK_TEXT, 'Find your route')
    """@type : Link"""

    regions_list = Find(WebElement, By.XPATH,
                        '//*[@class="panel panel-default"]/../%s' % my_config.ui_elements.ru.major_topo_name)
    """@type : WebElement"""

    sectors_list = Find(WebElement, By.XPATH,
                        '//*[@class="panel panel-default"]/../%s' % my_config.ui_elements.ru.minor_topo_name)
    """@type : WebElement"""

    first_region_in_list = Find(WebElement, By.XPATH, './/ul[@class="list-group list-group-area"]/li[1]')

    first_sector_in_list = Find(WebElement, By.XPATH, './/ul[@class="list-group list-group-sector"]/li[1]')

    map = Find(WebElement, By.ID, "map-canvas")
    """@type : WebElement"""

    def is_present(self):
        return self.is_element_present('page_locator')

    def is_news_tab_present(self):
        return self.is_element_present('news_tab')

    def is_news_link_present(self):
        return self.is_element_present('news_link')

    def is_login_present(self):
        return self.is_element_present('logged_user')

    def is_regions_list_present(self):
        return self.is_element_present('regions_list')

    def is_sectors_list_present(self):
        return self.is_element_present('sectors_list')

    def is_map_present(self):
        return self.is_element_present('map')

    def open_first_region(self):
        if self.is_regions_list_present():
            self.select_region_by_number(1).click()

    def select_region_by_number(self, number):
        if not number:
            number = 1
        return Find(WebElement, By.XPATH, './/ul[@class="list-group list-group-area"]/li[%i]' % number)

    def select_sector_by_number(self, number):
        if not number:
            number = 1
        return Find(WebElement, By.XPATH, './/ul[@class="list-group list-group-sector"]/li[%i]' % number)
