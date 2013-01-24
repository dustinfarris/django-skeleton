from fabric.api import env


env.project_name = '{{ project_name }}'
env.repo_source = 'git@github.com:yournamehere/{{ project_name }}.git'
env.django_settings_module = '{{ project_name }}.settings'
env.django_test_settings_module = '{{ project_name }}.settings.test'
# env.roledefs = {
#   'staging': ['web@12.12.12.12'],
#   'production': ['web@45.45.45.45']}


from automation import *
