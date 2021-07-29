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
        params = {"page":2}
        method = request.method.lower()
        data = mapping[method](url, params=params).json()
        return Response(data=data)
