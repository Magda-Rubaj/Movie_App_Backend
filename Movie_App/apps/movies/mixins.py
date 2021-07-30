from .serializers import MovieSerializer, MoviePartSerializer


class SwitchSerializerMixin:

    def dispatch(self, request, *args, **kwargs):
        mapping = {
            "get": MoviePartSerializer
        }
        serializer = mapping.get(request.method.lower(), MovieSerializer)
        return super().dispatch(request, *args, **kwargs)

