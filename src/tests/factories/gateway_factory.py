from factory import Factory, Faker

from gateway.models import Gateway


class GatewayFactory(Factory):
    id = Faker(provider="uuid4")
    name = Faker(provider="domain_word")
    mac_address = Faker("mac_address")

    class Meta:
        model = Gateway
