from django.apps import AppConfig


class UciAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UCI_App'

    def ready(self):
        import UCI_App.signals # register the signals