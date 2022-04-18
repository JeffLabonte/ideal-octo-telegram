from multiprocessing import Process
from typing import Callable

import pika


class BaseMQTT:
    EXCHANGE_NAME = "ideal_octo_telegram_topic"

    def __init__(self, hostname="localhost") -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self.channel = self.connection.channel()
        self.create_queue()

    def create_queue(self) -> None:
        self.channel.exchange_declare(exchange=self.EXCHANGE_NAME, exchange_type="topic")
        channel_result = self.channel.queue_declare("", exclusive=True)
        self.queue_name = channel_result.method.queue

    def close(self):
        self.connection.close()


class MQTTConsumerHandler(BaseMQTT):
    def __init__(self, hostname="localhost") -> None:
        self.process = None
        super().__init__(hostname=hostname)

    def bind_topic(self, topic: str, callback: Callable) -> None:
        self.channel.queue_bind(
            exchange=self.EXCHANGE_NAME,
            queue=self.queue_name,
            routing_key=topic,
        )
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )

    def start_process(self):
        self.process = Process(target=self.channel.start_consuming)
        self.process.start()

    def stop_process(self):
        self.process.kill()


class MQTTEmitHanlder:
    def __init__(self) -> None:
        pass
