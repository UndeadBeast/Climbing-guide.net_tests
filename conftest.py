from fixure.application import Application
from model.account import UserAccount
import pytest

__author__ = 'g_trofimov'


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.navigation.open_home_page()
    fixture.session.log_in(account=UserAccount())

    def fin():
        fixture.session.log_out()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
