import pytest


def test_simple_page(client):
    resp = client.get('/')
    assert resp.http_status == 200
