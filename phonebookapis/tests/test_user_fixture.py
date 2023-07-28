import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user():
    User = get_user_model()
    new_user = User.objects.create_user(
        email="test@gmail.com", password="test"
        )
    return new_user


@pytest.fixture
def superuser():
    User = get_user_model()
    new_superuser = User.objects.create_superuser(
        email="superuser@gmail.com", password="supertest"
    )
    return new_superuser
