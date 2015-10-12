# -*- coding: utf-8 -*-
import time


def test_add_ascend(app):
    old_my_ascends = app.ascend.get_ascends_list()
    time.sleep(2)
    app.ascend.add_hardcoded_ascend()
    time.sleep(2)
    new_my_ascends = app.ascend.get_ascends_list()
    assert len(old_my_ascends) + 1 == len(new_my_ascends)


def test_edit_ascend(app):
    if app.ascend.count() == 0:
        app.ascend.add_hardcoded_ascend()
    time.sleep(2)
    app.ascend.edit_first_element()


def test_delete_ascend(app):
    if app.ascend.count() == 0:
        app.ascend.add_hardcoded_ascend()
    time.sleep(2)
    old_my_ascends = app.ascend.get_ascends_list()
    time.sleep(2)
#    app.navigation.open_home_page()
    app.ascend.delete_first_element()
    time.sleep(2)
    new_my_ascends = app.ascend.get_ascends_list()
    assert len(old_my_ascends) - 1 == len(new_my_ascends)
