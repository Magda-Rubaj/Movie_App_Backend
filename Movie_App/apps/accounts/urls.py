from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .views import EmailTokenView, UserView


router = DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('obtain-token', EmailTokenView.as_view(), name='token_obtain'),
    path('refresh-token', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]