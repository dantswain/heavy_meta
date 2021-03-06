"""
Tests for the Song List view
"""

import pytest

from hm_web.models import Song

# pylint: disable=redefined-outer-name,missing-docstring,unused-argument

URL = '/songs'


@pytest.fixture
def songs(user):
    songs = [
        Song(title="Hipster Blues", created_by=user),
        Song(title="Hillbilly Rhapsody", created_by=user)
    ]

    for song in songs:
        song.save()

    return songs


@pytest.mark.django_db
def test_no_songs(client, logged_in_user):
    resp = client.get(URL)
    assert resp.status_code == 200
    assert "No songs" in resp.content.decode('utf-8')


@pytest.mark.django_db
def test_with_songs(client, songs, logged_in_user):
    resp = client.get(URL)
    assert resp.status_code == 200

    for song in songs:
        assert song.title in resp.content.decode('utf-8')


@pytest.mark.django_db
def test_login_required(client):
    resp = client.get(URL)
    assert resp.status_code == 302
    assert resp.url == '/login?next=/songs'
