"""
Tests for songs
"""

import pytest
assert pytest

from django.db import IntegrityError

from hm_web.models import Song

# pylint: disable=redefined-outer-name,missing-docstring


@pytest.fixture
def valid_song(user):
    return Song(
        title="Heavy Meta Tribute",
        note="This is a note",
        created_by=user
    )


@pytest.mark.django_db
def test_valid_song(valid_song):
    valid_song.save()
    assert isinstance(valid_song.id, int)
    assert valid_song.created_at
    assert valid_song.updated_at


@pytest.mark.django_db
def test_note_optional(valid_song):
    valid_song.note = None
    valid_song.save()
    assert isinstance(valid_song.id, int)


@pytest.mark.django_db
def test_title_required(valid_song):
    valid_song.title = None
    with pytest.raises(IntegrityError):
        valid_song.save()
