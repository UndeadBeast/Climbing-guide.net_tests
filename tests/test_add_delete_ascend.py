# -*- coding: utf-8 -*-
import time


def test_add_ascend(app):
    app.navigation.open_home_page()
    app.ascend.add()


def test_delete_ascend(app):
    app.navigation.open_home_page()
    app.ascend.delete_first_element()
