from django.core.cache import cache
from django.test import TestCase
from rest_framework.test import APITestCase


class TestCase(TestCase):
    """
    Same as Django built-in TestCase, but dumps the cache before every test.
    """
    def _pre_setup(self):
        cache.clear()
        super(TestCase, self)._pre_setup()


class APITestCase(APITestCase):
    """
    Same as REST Framework TestCase, but dumps the cache before every test.
    """
    def _pre_setup(self):
        cache.clear()
        super(APITestCase, self)._pre_setup()
