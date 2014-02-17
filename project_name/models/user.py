from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        app_label = '{{ project_name }}'
