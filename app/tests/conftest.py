import pytest
from django.core.management import call_command


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    """
    This causes an error later when Django uses default settings
    """
    from dynaconf import settings
    settings.configure(FORCE_ENV_FOR_DYNACONF='pytest')


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'project/fixtures/admin.json')
