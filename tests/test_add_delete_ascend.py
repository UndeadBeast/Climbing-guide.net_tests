# -*- coding: utf-8 -*-
import time


def test_add_ascend(app):
    app.ascend.add_hardcoded_ascend()


def test_edit_ascend(app):
    if app.ascend.count() == 0:
        app.ascend.add_hardcoded_ascend()
    time.sleep(2)
    app.ascend.edit_first_element()


def test_delete_ascend(app):
    if app.ascend.count() == 0:
        app.ascend.add_hardcoded_ascend()
    time.sleep(2)
#    app.navigation.open_home_page()
    app.ascend.delete_first_element()
