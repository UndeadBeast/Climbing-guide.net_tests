# -*- coding: utf-8 -*-
import time

import pytest
from model.account import UserAccount
from fixure.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_basic_checks(app):
    app.navigation.open_home_page()
    app.session.log_in(account=UserAccount())
    app.ascend.add()
    time.sleep(2)
    app.ascend.delete_first_element()
    app.session.log_out()
