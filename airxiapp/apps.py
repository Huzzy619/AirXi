from django.apps import AppConfig


class AirxiappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "airxiapp"

    def ready(self):
        import airxiapp.signals