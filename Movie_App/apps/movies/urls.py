from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieView


router = DefaultRouter()
router.register(r'movies', MovieView)

urlpatterns = [
    path('', include(router.urls)),
]