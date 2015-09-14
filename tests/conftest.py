from fixure.application import Application
import pytest

__author__ = 'g_trofimov'


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
