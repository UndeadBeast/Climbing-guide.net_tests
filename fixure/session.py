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

    def log_out(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.glyphicon.glyphicon-user").click()
        wd.find_element_by_link_text("Log out").click()
