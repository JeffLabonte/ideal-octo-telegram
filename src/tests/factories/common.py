from random import random
from factory.declarations import LazyAttribute


def lazy_random_attribute(choices: list) -> LazyAttribute:
    def get_random_choice(*args, **kwargs):
        choices_length = len(choices)
        return choices[random.randint(0, choices_length - 1)]

    return LazyAttribute(get_random_choice)
