# -*- coding: utf-8 -*-
from random import randrange
import time


def test_add_ascend(app):
    old_my_ascends = app.ascend.get_ascends_list()
    time.sleep(1)
    assert app.ascend.add_ascend() != 0
    time.sleep(1)
    assert len(old_my_ascends) + 1 == app.ascend.count()
    # new_my_ascends = app.ascend.get_ascends_list()


def test_edit_ascend(app):
    routes_count = app.ascend.count()
    if routes_count == 0:
        app.ascend.add_ascend()
        routes_count += 1
    index = randrange(routes_count)
    time.sleep(1)
    app.ascend.edit_ascend_by_index(index)


def test_delete_ascend(app):
    if app.ascend.count() == 0:
        app.ascend.add_ascend()
    time.sleep(1)
    old_my_ascends = app.ascend.get_ascends_list()
    index = randrange(len(old_my_ascends))
    time.sleep(1)
    app.ascend.delete_ascend_by_index(index)
    time.sleep(1)
    new_my_ascends = app.ascend.get_ascends_list()
    assert len(old_my_ascends) - 1 == app.ascend.count()
    old_my_ascends[index:index+1] = []
    assert sorted(old_my_ascends, key=id) == sorted(new_my_ascends, key=id)
