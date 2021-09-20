class DefaultIpAddress:
    """
    Get IP Address From Request
    """

    require_context = True

    def __call__(self, serializer_field):
        request = serializer_field["request"]  # TODO Run it to see where IPAddress
        pass
