import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'g_trofimov'


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def log_in(self, account):
        wd = self.app.wd
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("login-form-login").click()
        wd.find_element_by_id("login-form-login").clear()
        wd.find_element_by_id("login-form-login").send_keys(account.username)
        wd.find_element_by_id("login-form-password").click()
        wd.find_element_by_id("login-form-password").clear()
        wd.find_element_by_id("login-form-password").send_keys(account.password)
        wd.find_element_by_xpath("//form[@id='login-form']//button[.='Авторизоваться']").click()
        time.sleep(2)
        # element = wd.find_element_by_class_name("glyphicon glyphicon-user")
        # wait = WebDriverWait(wd, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "glyphicon glyphicon-user")))

    def log_out(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.glyphicon.glyphicon-user").click()
        wd.find_element_by_link_text("Log out").click()
