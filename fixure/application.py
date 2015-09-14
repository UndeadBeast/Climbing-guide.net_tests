from fixure.ascend import AscendHelper
from fixure.navigation import NavigationHelper
from fixure.session import SessionHelper
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = 'g_trofimov'


class Application():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.ascend = AscendHelper(self)
        self.navigation = NavigationHelper(self)

    def destroy(self):
        self.wd.quit()
