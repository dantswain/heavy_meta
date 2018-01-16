"""
Tests for navtags
"""

import pytest
assert pytest

from django.http import HttpRequest

from hm_web.templatetags import navtags


def build_request(path):
    """
    Build an HttpRequest object with the given path
    """
    request = HttpRequest()
    request.path = path
    return request


def test_home_active():
    assert navtags.active(build_request('/'), '/') == 'active'
    assert navtags.active(build_request('/login'), '/') == ''


def test_login_active():
    assert navtags.active(build_request('/'), '/login') == ''
    assert navtags.active(build_request('/login'), '/login') == 'active'
