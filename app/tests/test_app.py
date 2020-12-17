import django

django.setup()  # noqa

import pytest

from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_admin_user():
    User = get_user_model()

    assert User.objects.filter(username='admin').exists()


@pytest.mark.django_db
def test_another():
    User = get_user_model()

    assert User.objects.filter(username='admin').exists()
