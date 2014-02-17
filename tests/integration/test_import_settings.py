from django.test import TestCase


class SettingsImportTest(TestCase):
    """
    We should be able to import our own settings, and DEBUG should
    be False.
    """
    def test_import_settings(self):
        from django.conf import settings
        assert settings.DEBUG is False
