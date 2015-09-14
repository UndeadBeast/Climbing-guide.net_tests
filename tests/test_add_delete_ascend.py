# -*- coding: utf-8 -*-
import time

from model.account import UserAccount


def test_basic_checks(app):
    app.navigation.open_home_page()
    app.session.log_in(account=UserAccount())
    app.ascend.add()
    time.sleep(2)
    app.ascend.delete_first_element()
    app.session.log_out()
