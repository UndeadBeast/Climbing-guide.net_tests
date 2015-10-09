from fixure import my_config

__author__ = 'g_trofimov'


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        self.app.wd.get("http://climbing-guide.net/")

    def open_my_routes_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("my-routes") \
                and len(wd.find_elements_by_link_text(my_config.config_file.ui_locale.ru.my_routes)) > 0:
            return
        wd.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-1']/ul[2]/li[5]/a").click()
        wd.find_element_by_link_text("Мои трассы").click()
