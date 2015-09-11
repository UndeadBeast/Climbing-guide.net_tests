# -*- coding: utf-8 -*-
import unittest
import time
from account import UserAccount
from ascend import Ascend

from selenium.webdriver.firefox.webdriver import WebDriver


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://climbing-guide.net/ru")

    def log_in(self, wd, account):
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("login-form-login").click()
        wd.find_element_by_id("login-form-login").clear()
        wd.find_element_by_id("login-form-login").send_keys(account.username)
        wd.find_element_by_id("login-form-password").click()
        wd.find_element_by_id("login-form-password").clear()
        wd.find_element_by_id("login-form-password").send_keys(account.password)
        wd.find_element_by_xpath("//form[@id='login-form']//button[.='Авторизоваться']").click()

    def log_out(self, wd):
        wd.find_element_by_css_selector("span.glyphicon.glyphicon-user").click()
        wd.find_element_by_link_text("Log out").click()

    def add_ascend(self, wd, ascend_date="04-09-2015", ascend_comment="qa test"):
        # select region
        wd.find_element_by_css_selector("li.list-group-item > div").click()
        # select sector
        wd.find_element_by_link_text("Центральный").click()
        wd.find_element_by_xpath("//tr[@id='route-id-7']/td[6]/button").click()
        wd.find_element_by_css_selector("div.modal-footer > button.btn.btn-default").click()
        wd.find_element_by_css_selector("td.td-route-name").click()
        wd.find_element_by_xpath("//div[@class='panel-body']/p/span").click()
        wd.find_element_by_css_selector("#userroutes-ascent_type > label").click()
        if not wd.find_element_by_xpath("//div[@id='userroutes-ascent_type']/label[1]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='userroutes-ascent_type']/label[1]/input").click()
        wd.find_element_by_id("userroutes-date").click()
        wd.find_element_by_id("userroutes-date").clear()
        wd.find_element_by_id("userroutes-date").send_keys(ascend_date)
        wd.find_element_by_id("userroutes-comment").click()
        if not wd.find_element_by_xpath("//div[@id='userroutes-vote']/label[1]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='userroutes-vote']/label[1]/input").click()
        if not wd.find_element_by_xpath("//div[@class='modal-body']/div[2]/div[1]/div/select//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@class='modal-body']/div[2]/div[1]/div/select//option[1]").click()
        wd.find_element_by_id("userroutes-comment").click()
        wd.find_element_by_id("userroutes-comment").clear()
        wd.find_element_by_id("userroutes-comment").send_keys(ascend_comment)
        wd.find_element_by_css_selector("div.modal-footer > button.btn.btn-success").click()

    def delete_ascend(self, wd):
        wd.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-1']/ul[2]/li[5]/a").click()
        wd.find_element_by_link_text("Мои трассы").click()
        wd.find_element_by_xpath("//div[@id='w0']/table/tbody/tr/td[6]/a").click()

    def test_basic_checks(self):
        wd = self.wd
        self.open_home_page(wd)
        self.log_in(wd, account=UserAccount())
        self.add_ascend(wd)
        time.sleep(2)
        self.delete_ascend(wd)
        self.log_out(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
