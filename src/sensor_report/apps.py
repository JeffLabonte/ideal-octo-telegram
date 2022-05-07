from multiprocessing.context import Process
from threading import Timer
from django.apps import AppConfig

from mqtt_integration.mqtt_handler import MQTTConsumerHandler


def callback(ch, method, properties, body):
    print(locals())


class SensorReportConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sensor_report"

    def ready(self):
        self.connect_mqtt()

        return super().ready()

    def connect_mqtt(self):
        try:
            self.consumer_mqtt = MQTTConsumerHandler()
            self.consumer_mqtt.bind_topic(topic="#", callback=callback)
            self.consumer_mqtt.start_process()
        except Exception as ex:
            print(f"Unable to connect to MQTT Broker: {ex}")
            Process(target=self.retry, daemon=True).start()

    def retry(self):
        Timer(interval=10, function=self.connect_mqtt).start()
