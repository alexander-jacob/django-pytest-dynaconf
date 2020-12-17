import django
from django.conf import settings

django.setup()  # noqa

import pytest

from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_admin_user():
    User = get_user_model()

    assert User.objects.filter(username='admin').exists()


def test_settings():
    assert settings.FOO == 'foo-test'
