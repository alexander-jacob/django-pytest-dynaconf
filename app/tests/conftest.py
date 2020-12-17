import pytest
from django.core.management import call_command


@pytest.fixture(scope="session", autouse=True)
def assert_dynaconf_pytest_environment():
    from django.conf import settings
    assert settings.ENVIRONMENT == 'pytest'


@pytest.fixture(autouse=True)
def fixtures(db):
    call_command('loaddata', 'project/fixtures/admin.json')
