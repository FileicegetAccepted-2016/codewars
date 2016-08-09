from django import template

register = template.Library()

from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re



