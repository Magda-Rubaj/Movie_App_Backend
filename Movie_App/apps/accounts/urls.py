from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import EmailTokenView


urlpatterns = [
    path('obtain-token', EmailTokenView.as_view(), name='token_obtain'),
    path('refresh-token', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]