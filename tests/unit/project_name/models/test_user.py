from django.contrib.auth.models import AbstractUser
from django.test import TestCase

from {{ project_name }}.models import User


class UserTests(TestCase):
    def test_user_inherits_from_abstract_user(self):
        assert isinstance(User(), AbstractUser)
