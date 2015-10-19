import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'g_trofimov'


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def log_in(self, user_account):
        wd = self.app.wd
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("login-form-login").click()
        wd.find_element_by_id("login-form-login").clear()
        wd.find_element_by_id("login-form-login").send_keys(user_account.username)
        wd.find_element_by_id("login-form-password").click()
        wd.find_element_by_id("login-form-password").clear()
        wd.find_element_by_id("login-form-password").send_keys(user_account.password)
        wd.find_element_by_xpath("//form[@id='login-form']//button[.='Авторизоваться']").click()
        time.sleep(2)
        # element = wd.find_element_by_class_name("glyphicon glyphicon-user")
        # wait = WebDriverWait(wd, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "glyphicon glyphicon-user")))

    def log_out(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.glyphicon.glyphicon-user").click()
        wd.find_element_by_link_text("Log out").click()

    def is_log_in(self):
        wd = self.app.wd
        if len(wd.find_element_by_css_selector("span.glyphicon.glyphicon-user")) > 0:
            return True

    def check_login(self, user_account=None, do_login=True, do_logout=False):
        """Check is user logged in
        If user isn't given  - check only logged in or not
        if user is given - check is it actual user or not

        Keyword arguments:
        username - string
        do_login - should method process login
        do_logout - should method process logout
        """
        wd = self.app.wd
        # is login available
        if len(wd.find_elements_by_link_text("Log in")) > 0:
            if do_login:
                self.log_in(user_account)
        # is logout available
        elif len(wd.find_elements_by_css_selector("span.glyphicon.glyphicon-user")) > 0:
            if user_account is None and do_logout:
                self.log_out()
            else:
                # check if email from parameter is actual user email
                wd.get("http://climbing-guide.net/ru/user/settings/account")
                current_user_email = wd.find_element_by_xpath(
                    "//div[@class='panel-heading']/*[.//span[contains(@class, 'glyphicon-user')]]").text
                if current_user_email != user_account.email:
                    if do_login:
                        self.log_in(user_account)
        else:
            print("State Unknown! If user logged in or not can not be defined!")


