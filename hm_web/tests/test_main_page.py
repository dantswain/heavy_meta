import pytest


assert pytest


def test_simple_page(client):
    resp = client.get('/')
    assert resp.status_code == 200
