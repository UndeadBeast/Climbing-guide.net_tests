# -*- coding: utf-8 -*-
from fixure.utilities import WebUtilities
from model.route import Rout
from selenium.webdriver.common.by import By

__author__ = 'g_trofimov'


class AscendHelper:
    def __init__(self, app):
        self.app = app

    my_ascends_list = None

    def add_ascend(self, ascend_date="04-09-2015", ascend_comment="qa test", region_name="Буки",
                   sector_name="Центральный", route_name="Щелеход"):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        # select region
        wd.find_element_by_xpath("//li[@class='list-group-item']//*[contains(text(), {0})]".format(region_name)).click()
        # select sector
        wd.find_element_by_link_text(sector_name).click()
        # open route detail
        current_route = wd.find_element_by_xpath("//tr[@data-name='{0}']".format(route_name))
        route_id = current_route.get_attribute("data-route")
        # if current_route.is_element_present(how=By.XPATH, what=".//button[contains(@class, 'add-route-ascent-btn')]"):
        if len(current_route.find_elements_by_xpath(".//button[contains(@class, 'add-route-ascent-btn')]")) != 0:
            current_route.find_element_by_xpath(".//button[contains(@class, 'add-route-ascent-btn')]").click()
        else:
            # TODO: add deletion of ascend for this route
            print(
                "Ascend for rout {0} -> {1} -> {2} already exists! Please, delete it!".format(region_name, sector_name,
                                                                                              route_name))
            return 0
        # open "add_ascend ascend" form routs list
        wd.find_element_by_css_selector("td.td-route-name").click()
        # open route detail
        # # click "add ascend" button
        # wd.find_element_by_xpath("//div[@class='panel-body']/p/span").click()
        # fill ascend
        wd.find_element_by_css_selector("#userroutes-ascent_type > label").click()
        if not wd.find_element_by_xpath("//div[@id='userroutes-ascent_type']/label[1]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='userroutes-ascent_type']/label[1]/input").click()
        wd.find_element_by_id("userroutes-date").click()
        wd.find_element_by_id("userroutes-date").clear()
        wd.find_element_by_id("userroutes-date").send_keys(ascend_date)
        # wd.find_element_by_id("userroutes-comment").click()
        if not wd.find_element_by_xpath("//div[@id='userroutes-vote']/label[1]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='userroutes-vote']/label[1]/input").click()
        if not wd.find_element_by_xpath("//div[@class='modal-body']/div[2]/div[1]/div/select//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@class='modal-body']/div[2]/div[1]/div/select//option[1]").click()
        wd.find_element_by_id("userroutes-comment").click()
        wd.find_element_by_id("userroutes-comment").clear()
        wd.find_element_by_id("userroutes-comment").send_keys(ascend_comment)
        wd.find_element_by_css_selector("div.modal-footer > button.btn.btn-success").click()
        self.my_ascends_list = None
        return route_id

    def fill_ascend_form(self, ascend_date="01-09-2015", ascend_comment="qa test", ascend_type=1, category=2):
        wd = self.app.wd
        # fill ascend type
        if not wd.find_element_by_xpath(
                        "//div[@id='userroutes-ascent_type']/label[%s]/input" % ascend_type).is_selected():
            wd.find_element_by_xpath("//div[@id='userroutes-ascent_type']/label[%s]/input" % ascend_type).click()
        # fill date.
        wd.find_element_by_id("userroutes-date").click()
        wd.find_element_by_id("userroutes-date").clear()
        wd.find_element_by_id("userroutes-date").send_keys(ascend_date)
        # fill vote. Now - dislike
        if not wd.find_element_by_xpath("//div[@id='userroutes-vote']/label[2]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='userroutes-vote']/label[2]/input").click()
        # fill category.
        if not wd.find_element_by_xpath(
                        "//div[@class='modal-body']/div[2]/div[1]/div/select//option[%s]" % category).is_selected():
            wd.find_element_by_xpath(
                "//div[@class='modal-body']/div[2]/div[1]/div/select//option[%s]" % category).click()
        # fill comment
        wd.find_element_by_id("userroutes-comment").click()
        wd.find_element_by_id("userroutes-comment").clear()
        wd.find_element_by_id("userroutes-comment").send_keys(ascend_comment)
        # save changes
        wd.find_element_by_css_selector("div.modal-footer > button.btn.btn-success").click()

    def edit_ascend_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_my_routes_page()
        wd.find_elements_by_xpath("//div[@id='w0']/table/tbody/tr/td[6]/button")[index].click()
        self.fill_ascend_form(ascend_date="01-01-2014", ascend_comment="qa test edit")
        self.my_ascends_list = None

    def delete_ascend_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_my_routes_page()
        wd.find_elements_by_xpath("//div[@id='w0']/table/tbody/tr/td[6]/a")[index].click()
        self.my_ascends_list = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_my_routes_page()
        return len(wd.find_elements_by_xpath("//div[@id='w0']//tr[@data-key]"))
        # return len(wd.find_elements_by_xpath("//tr[@data-key]"))

    def get_ascends_list(self):
        if self.my_ascends_list is None:
            wd = self.app.wd
            self.app.navigation.open_my_routes_page()
            self.my_ascends_list = []
            for element in wd.find_elements_by_xpath("//tr[@data-key]"):
                route_id = element.get_attribute("data-key")
                route_name = element.find_element_by_xpath(".//td[2]").text
                self.my_ascends_list.append(Rout(name=route_name, id=route_id))
        return list(self.my_ascends_list)
