from tests.utils import TestCase


class SettingsImportTest(TestCase):
    """
    Check that we can import our own settings and that DEBUG is False
    when testing.
    """
    def test_import_settings(self):
        from django.conf import settings
        assert settings.DEBUG is False
