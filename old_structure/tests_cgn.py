from grail import BaseTest
# import steps_basic
from old_structure import steps_page_check

__author__ = 'g_trofimov'


class CGNTests(BaseTest):
    # cgn_steps = steps_basic.CGNBasicSteps()
    cgn_page_check = steps_page_check.CGNPageCheckSteps()

    # def test_check_pages_test(self):
    #     self.cgn_page_check.check_page_main()
    #     self.cgn_page_check.check_page_my_routes()

    def test_main_page_checks(self):
        self.cgn_page_check.main_page_check()

    # def test_user_route_activity(self):
    #     self.cgn_steps.log_in()
    #     self.cgn_steps.add_my_route_with_default_topography()
    #     time.sleep(2)
    #     self.cgn_steps.remove_my_route_with_default_topography()
    #     self.cgn_steps.log_out()

    # @classmethod
    # def teardown_class(cls):
    #     cls.browser.quit_browser()
