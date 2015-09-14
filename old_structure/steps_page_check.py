from grail import step
from nose.tools import ok_
from selenium import webdriver
from fixure.my_config import CGN_URL
from pages.home_page import CGNHomePage

__author__ = 'g_trofimov'


class CGNPageCheckSteps(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(CGN_URL)
        self.home_page = CGNHomePage(url=CGN_URL)

    @step
    def main_page_check(self):
        ok_(self.home_page.is_present(), 'Main page is not present')
        ok_(self.home_page.is_regions_list_present(), 'region list is not present')
        ok_(self.home_page.is_sectors_list_present(), 'sectors list is not present')
        ok_(self.home_page.is_map_present(), 'map is absent')
        ok_(self.home_page.is_home_button_present(), 'Home button is absent')
        self.home_page.select_region_by_number(1)
        self.home_page.select_sector_by_number(1)
        self.home_page.open_home_page()
