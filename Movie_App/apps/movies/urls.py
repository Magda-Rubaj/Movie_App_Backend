from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieView, ActorView


router = DefaultRouter()
router.register(r'movies', MovieView)
router.register(r'actors', ActorView)

urlpatterns = [
    path('', include(router.urls)),
]