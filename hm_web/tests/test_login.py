"""
Tests for logging in and out
"""
import pytest
from django.contrib import auth
from django.contrib.auth.models import User


# pylint: disable=redefined-outer-name


PASSWORD = 'abc123'


@pytest.fixture
def user():
    """
    Returns a user model
    """
    the_user = User\
        .objects\
        .create_user(username='test_user',
                     email='foo@bar.com',
                     password=PASSWORD)
    return the_user


def test_login_page(client):
    resp = client.get('/login')
    assert resp.status_code == 200


def test_logout_page(client):
    resp = client.get('/logout')
    assert resp.status_code == 302
    assert resp.url == '/'


@pytest.mark.django_db
def test_login(user, client):
    resp = client.post('/login',
                       {'username': user.username, 'password': PASSWORD})
    assert resp.status_code == 302
    assert resp.url == '/'

    logged_in_user = auth.get_user(client)
    assert logged_in_user.email == user.email
    assert logged_in_user.is_authenticated


@pytest.mark.django_db
def test_invalid_login(user, client):
    resp = client.post('/login',
                       {'username': user.username, 'password': 'wrong'})
    assert resp.status_code == 200

    logged_in_user = auth.get_user(client)
    assert not logged_in_user.is_authenticated


@pytest.mark.django_db
def test_logout_not_logged_in(client):
    resp = client.post('/logout')
    assert resp.status_code == 302
    assert resp.url == '/'

    logged_in_user = auth.get_user(client)
    assert not logged_in_user.is_authenticated


@pytest.mark.django_db
def test_logout_post(user, client):
    client.login(username=user.username, password=PASSWORD)

    resp = client.post('/logout')
    assert resp.status_code == 302
    assert resp.url == '/'

    logged_in_user = auth.get_user(client)
    assert not logged_in_user.is_authenticated
