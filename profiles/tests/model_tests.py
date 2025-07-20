import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create_user(username='testuser', password='testpass')
    profile = Profile.objects.get(user=user)
    assert str(profile) == 'testuser'


@pytest.mark.django_db
def test_profile_auto_created_on_user_creation():
    user = User.objects.create_user(username='newuser', password='password')
    # Profile should be auto-created by post_save signal
    profile = Profile.objects.filter(user=user).first()
    assert profile is not None
    assert profile.user == user


@pytest.mark.django_db
def test_profile_updated_on_user_save():
    user = User.objects.create_user(username='updateuser', password='password')
    profile = Profile.objects.get(user=user)
    # Change something on user and save, profile.save() is called by signal
    user.first_name = 'Updated'
    user.save()

    # Fetch profile again to confirm still exists and linked
    updated_profile = Profile.objects.get(user=user)
    assert updated_profile == profile
