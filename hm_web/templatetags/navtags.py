"""
Custom template tags used in the navbar
"""
from django import template

# pylint: disable=invalid-name
register = template.Library()

@register.simple_tag
def active(request, pattern):
    """
    Returns 'active' if request's path matches the given pattern
    """
    if request.path == pattern:
        return 'active'
    else:
        return ''
