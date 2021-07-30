from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'movies', views.MovieView)
router.register(r'actors', views.ActorView)
router.register(r'directors', views.DirectorView)

urlpatterns = [
    path('', include(router.urls)),
    path('external/', views.ExternalApiView.as_view()),
]