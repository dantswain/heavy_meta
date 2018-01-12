"""
Tests for index.html
"""

import pytest


assert pytest


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
