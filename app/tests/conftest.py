import pytest
from django.core.management import call_command


@pytest.fixture(scope="session", autouse=True)
def assert_dynaconf_pytest_environment():
    from django.conf import settings
    assert settings.ENVIRONMENT == 'pytest'


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'project/fixtures/admin.json')
