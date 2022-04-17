import pika


class BaseMQTT:
    def __init__(self, hostname="localhost") -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self.channel = self.connection.channel()

    def create_queue(self, queue_name: str) -> None:
        self.channel.queue_declare(queue=queue_name)


class MQTTConsumerHandler:
    def __init__(self) -> None:
        pass


class MQTTEmitHanlder:
    def __init__(self) -> None:
        pass
