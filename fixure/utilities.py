from fixure.my_config import config_file
from selenium.common.exceptions import NoSuchElementException

__author__ = 'g_trofimov'


class WebUtilities():
    def __init__(self, app):
        self.app = app

    def is_element_present(self, how, what):
        wd = self.app.wd
        wd.implicitly_wait(0)
        try:
            wd.find_element(by=how, value=what)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            wd.implicitly_wait(config_file.implicitly_timeout)
