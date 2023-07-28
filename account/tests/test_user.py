import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_new_user(user):
    User = get_user_model()
    count = User.objects.all().count()
    assert count == 1

    existing_user = user
    new_user = User.objects.first()
    assert existing_user.id == new_user.id
    assert new_user.email == "test@gmail.com"
    assert new_user.is_staff == 0
    assert new_user.is_active == 1
    assert new_user.is_superuser == 0
    with pytest.raises(TypeError):
        User.objects.create_user()


@pytest.mark.django_db
def test_new_superuser(superuser):
    User = get_user_model()
    count = User.objects.all().count()
    assert count == 1

    existing_superuser = superuser
    new_superuser = User.objects.first()
    assert new_superuser == existing_superuser
    assert new_superuser.email == "superuser@gmail.com"
    assert new_superuser.is_staff == 1
    assert new_superuser.is_active == 1
    assert new_superuser.is_superuser == 1
    with pytest.raises(TypeError):
        User.objects.create_superuser()
