"""
Common test code & fixtures
"""

import pytest

from django.contrib.auth.models import User

from hm_web.models import Song

# pylint: disable=redefined-outer-name,missing-docstring


@pytest.fixture
def password():
    return 'abc123'


@pytest.fixture
def user(password):
    """
    Returns a user model
    """
    the_user = User\
        .objects\
        .create_user(username='test_user',
                     email='foo@bar.com',
                     password=password)
    return the_user

@pytest.fixture
def logged_in_user(user, password, client):
    client.login(username=user.username, password=password)

    return user

@pytest.fixture
def song(user):
    song = Song(title="Travolta",
                created_by=user)
    song.save()
    return song
