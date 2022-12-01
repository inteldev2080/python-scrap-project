from django.urls import path
from .views import CryptoAPIView


urlpatterns = [
    path('', CryptoAPIView.as_view())
]