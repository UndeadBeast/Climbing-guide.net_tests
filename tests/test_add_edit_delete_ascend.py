# -*- coding: utf-8 -*-
import time


def test_basic_checks(app):
    app.navigation.open_home_page()
    app.ascend.add()
    time.sleep(2)
    app.navigation.open_my_routes_page()
    app.ascend.edit_first_element()
    time.sleep(2)
    app.ascend.delete_first_element()
