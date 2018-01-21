"""
Common test code & fixtures
"""

import pytest

from django.contrib.auth.models import User

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
