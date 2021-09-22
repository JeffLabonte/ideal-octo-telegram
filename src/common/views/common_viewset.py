from rest_framework.viewsets import GenericViewSet


class CommonViewSet(GenericViewSet):
    def get_serializer_class(self):
        if not getattr(self, "serializer_class", {}):
            raise NotImplementedError("You need to implement `serializer_class`")

        return self.serializer_class.get(self.action)
