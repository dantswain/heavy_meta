"""
Tests for index.html
"""

import pytest

# pylint: disable=unused-argument


def template_used(resp, template_name):
    """
    Returns True if the given template was used
    """
    for template in resp.templates:
        if template.name == template_name:
            return True

    return False


def test_simple_page(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert template_used(resp, 'hm_web/index.html')


@pytest.mark.django_db
def test_logged_in_redirects(client, logged_in_user):
    resp = client.get('/')
    assert resp.status_code == 302
    assert resp.url == '/songs'
