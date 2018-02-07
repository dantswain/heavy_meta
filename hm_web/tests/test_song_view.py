"""
Tests for the view of a single song
"""

import pytest

# pylint: disable=redefined-outer-name,missing-docstring,unused-argument

def song_url(song):
    return '/songs/{}'.format(song.id)


@pytest.mark.django_db
def test_song_view(client, logged_in_user, song):
    resp = client.get(song_url(song))
    assert resp.status_code == 200
    assert song.title in resp.content.decode('utf-8')


@pytest.mark.django_db
def test_not_found(client, logged_in_user):
    resp = client.get('/songs/0')
    assert resp.status_code == 404


@pytest.mark.django_db
def test_login_required(client, song):
    url = song_url(song)
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == '/login?next={}'.format(url)
