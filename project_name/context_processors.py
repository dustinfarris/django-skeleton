from django.conf import settings


def google(request):
  context = None
  if hasattr(settings, 'GOOGLE_UA'):
    context = {'GOOGLE_UA': settings.GOOGLE_UA}
  return context or {}