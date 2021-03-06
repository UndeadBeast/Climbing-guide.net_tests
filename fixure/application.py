from fixure.ascend import AscendHelper
from fixure.my_config import config_file
from fixure.navigation import NavigationHelper
from fixure.session import SessionHelper
from fixure.utilities import WebUtilities
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = 'g_trofimov'


class Application():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(config_file.implicitly_timeout)
        self.session = SessionHelper(self)
        self.ascend = AscendHelper(self)
        self.navigation = NavigationHelper(self)
        self.utils = WebUtilities(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except ValueError:
            print(ValueError)
            return False

    def destroy(self):
        self.wd.quit()
