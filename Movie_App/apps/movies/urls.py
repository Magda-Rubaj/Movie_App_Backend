from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieView, ActorView, DirectorView


router = DefaultRouter()
router.register(r'movies', MovieView)
router.register(r'actors', ActorView)
router.register(r'directors', DirectorView)

urlpatterns = [
    path('', include(router.urls)),
]