# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.conf import settings
from {{ project_name }}.context_processors import google
from {{ project_name }}.testutils import TestCase


class GoogleTest(TestCase):

    def test_google(self):
        settings.GOOGLE_UA = '12345'
        self.assertEqual({'GOOGLE_UA': '12345'}, google("RequestMock"))
