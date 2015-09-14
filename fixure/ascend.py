__author__ = 'g_trofimov'


class AscendHelper:
    def __init__(self, app):
        self.app = app

    def add(self, ascend_date="04-09-2015", ascend_comment="qa test"):
        wd = self.app.wd
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

    def delete_first_element(self):
        wd = self.app.wd
        self.app.navigation.open_my_routes_page()
        wd.find_element_by_xpath("//div[@id='w0']/table/tbody/tr/td[6]/a").click()
