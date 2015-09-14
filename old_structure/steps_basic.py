# -*- coding: utf-8 -*-
# from common.ui.core.browser import Browser
from grail import step
from old_structure import my_config
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from model.account import UserAccount
from old_structure.my_config import CGN_URL
from pages.home_page import CGNHomePage
from old_structure.screenshooter import ScreenshotListener

__author__ = 'g_trofimov'


class CGNBasicSteps(object):
    user = None
    firefox_driver = webdriver.Firefox()
    driver = EventFiringWebDriver(firefox_driver, ScreenshotListener())
    home_page = CGNHomePage(url=CGN_URL)


    def __init__(self):
        # self.browser = Browser()
        # home_page = HomePage()
        # page_404 = Page404("/not_existing")
        # navigationPanel = NavigationPanel()
        # controlPanel = controlPanel()
        # self.driver = EventFiringWebDriver(self.firefox_driver, ScreenshotListener())
        self.driver.implicitly_wait(my_config.implicitly_timeout)
        # self.base_url = self.cfg.base_url
        self.driver.get(CGN_URL)
        self.current_region = my_config.test_data.ru.region_name
        self.current_sector = my_config.test_data.ru.sector_name
        self.current_route = my_config.test_data.ru.route_name

    @step
    def log_in(self):
        driver = self.driver
        user = UserAccount()
        user.read_default_settings_from_config()
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("login-form-login").clear()
        driver.find_element_by_id("login-form-login").send_keys(user.email)
        driver.find_element_by_id("login-form-password").clear()
        driver.find_element_by_id("login-form-password").send_keys(user.password)
        driver.find_element_by_id("login-form-rememberme").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()

    @step
    def add_my_route_with_default_topography(self):
        driver = self.driver
        # Click region
        # driver.find_element_by_css_selector("li.list-group-item > div").click()
        region_element = driver.find_element_by_xpath(u"//li[@data-name=\"%s\"]/div[1]" % self.current_region)
        region_element.click()
        region_element.click()
        sector_element = driver.find_element_by_link_text(self.current_sector)
        sector_element.click()
        # Click route string in routes list inside of sector
        route_element = driver.find_element_by_xpath(
            u"//tr[@data-name='%s']/td[@class='td-route-name']" % self.current_route)
        route_element.click()
        # Click "add ascent"
        # driver.find_element_by_xpath("//p[@onclick=\"applyParamsToAscentRouteModal(8, 'Insight', 20)\"]").click()
        my_route = driver.find_element_by_xpath("//p[contains(@onclick,'%s')]" % self.current_route)
        my_route.click()
        # Fill "My Ascent" params and submit
        driver.find_element_by_css_selector("label > input[name=\"UserRoutes[ascent_type]\"]").click()
        driver.find_element_by_id("userroutes-date").click()
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_css_selector("label > input[name=\"UserRoutes[vote]\"]").click()
        Select(driver.find_element_by_id("userroutes-category_opinion")).select_by_visible_text("Project")
        driver.find_element_by_id("userroutes-comment").clear()
        driver.find_element_by_id("userroutes-comment").send_keys("QA test")
        driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-success").click()
        # assert()

    @step
    def remove_my_route_with_default_topography(self):
        driver = self.driver
        # Entering "My routes"
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-1']/ul[2]/li[5]/a").click()
        driver.find_element_by_link_text(my_config.ui_elements.ru.my_routes).click()
        # check is it there
        # if driver.find_element_by_class_name("empty") = true
        # delete route
        driver.find_element_by_xpath("//div[@id='w0']/table/tbody/tr/td[6]/a").click()
        # wait "Ничего не найдено"

    @step
    def view_random_regions_sectors_routs(self):
        driver = self.driver
        driver.find_element_by_css_selector("li.list-group-item > div").click()

    @step
    def log_out(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-1']/ul[2]/li[5]/a").click()
        driver.find_element_by_link_text("Log out").click()

    # def tearDown(self):
    #     if sys.exc_info()[0]:  # Returns the info of exception being handled
    #         fail_url = self.driver.current_url
    #         print fail_url
    #         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
    #         screenshot_path = '//d/Home/Dropbox/War/PycharmProjects/logs/%s.png' % now
    #         self.driver.get_screenshot_as_file(screenshot_path)
    #         # fail_screenshot_url = 'http://debugtool/screenshots/%s.png' % now
    #         print screenshot_path
    #     self.driver.quit()

    def main_page_check(self):
        self.home_page.is_present()
        self.home_page.is_regions_list_present()
        self.home_page.is_sectors_list_present()
        self.home_page.is_map_present()
        self.home_page.is_home_button_present()
        self.home_page.select_region_by_number(1)
        self.home_page.select_sector_by_number(1)
        self.home_page.open_home_page()
