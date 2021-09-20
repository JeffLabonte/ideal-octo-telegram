from django.apps import AppConfig


class SensorsConfig(AppConfig):
    name = "sensors"

    def ready(self):
        return super().ready()
