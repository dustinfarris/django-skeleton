from fabric.api import env


env.project_name = '{{ project_name }}'
env.django_settings_module = '{{ project_name }}.settings'
env.django_test_settings_module = '{{ project_name }}.settings.test'
# env.roledefs = {
#   'staging': 'web@12.12.12.12',
#   'production': 'web@45.45.45.45'}


from automation import *
