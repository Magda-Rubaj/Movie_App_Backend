from .serializers import MovieSerializer, MoviePartSerializer
import json
from rest_framework.response import Response
import requests


class SwitchSerializerMixin:

    def dispatch(self, request, *args, **kwargs):
        mapping = {
            "get": MoviePartSerializer
        }
        serializer = mapping.get(request.method.lower(), MovieSerializer)
        return super().dispatch(request, *args, **kwargs)


class ExternalCallMixin:

    def call_api(self, request, url, *args, **kwargs):
        mapping = {
            "get": requests.get
        }
        method = request.method.lower()

        return Response(mapping[method](url, data=json.dumps(request.data)).json())
