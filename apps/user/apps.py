from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'
    verbose_name = 'User'
    label = 'user'

    def ready(self):
        import apps.user.signals
