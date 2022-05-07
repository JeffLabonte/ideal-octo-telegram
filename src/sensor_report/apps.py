from django.apps import AppConfig

from mqtt_integration.mqtt_handler import MQTTConsumerHandler


def callback(ch, method, properties, body):
    print(locals())


class SensorReportConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sensor_report"

    def ready(self):
        self.consumer_mqtt = MQTTConsumerHandler()
        self.consumer_mqtt.bind_topic(topic="#", callback=callback)
        self.consumer_mqtt.start_process()

        return super().ready()
