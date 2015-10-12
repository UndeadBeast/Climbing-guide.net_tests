import time
from fixure.application import Application
from model.account import UserAccount
import pytest

__author__ = 'g_trofimov'

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.navigation.open_home_page()
    fixture.session.check_login(user_account=UserAccount(), do_login=True, do_logout=False)

    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # TODO logout processing to long = wd.implicitly_wait. Let's make it shorter!
        fixture.session.check_login(do_login=False, do_logout=True)
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
