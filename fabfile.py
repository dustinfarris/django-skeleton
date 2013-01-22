from fabric.api import env


env.django_settings_module = '{{ project_name }}.settings'
env.django_test_settings_module = '{{ project_name }}.settings.test'
# env.staging_server = {
#   'host': '12.12.12.12',
#   'user': 'web'}
# env.production_server = {
#   'host': '45.45.45.45',
#   'user': 'web'}


from automation import *
