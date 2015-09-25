# -*- coding: utf-8 -*-
import time


def test_add_ascend(app):
    app.navigation.open_home_page()
    app.ascend.add()


def test_edit_ascend(app):
    time.sleep(2)
    app.navigation.open_my_routes_page()
    app.ascend.edit_first_element()


def test_delete_ascend(app):
    time.sleep(2)
    app.navigation.open_home_page()
    app.ascend.delete_first_element()
