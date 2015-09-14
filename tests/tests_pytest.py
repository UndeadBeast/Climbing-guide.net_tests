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
    app.open_home_page()
    app.log_in(account=UserAccount())
    app.add_ascend()
    time.sleep(2)
    app.delete_ascend()
    app.log_out()
