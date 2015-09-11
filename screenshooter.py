from datetime import datetime
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

__author__ = 'g_trofimov'


class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        screenshot_name = "exception_%s.png" % datetime.now()
        driver.get_screenshot_as_file('/Screenshots/' + screenshot_name)
        print("Screenshot saved as '%s'" % screenshot_name)
