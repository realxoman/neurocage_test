from django.apps import AppConfig


class CagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cages'

    def ready(self):
        import cages.signals