# -*- coding: utf-8 -*-

from __future__ import absolute_import

from {{ project_name }}.testutils import TestCase


class SettingsImportTest(TestCase):

    def test_import_settings(self):
        from {{ project_name }}.settings import settings
        assert settings.DEBUG is False
