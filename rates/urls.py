from django.urls import path

from rates.views import RubRateAPIView


urlpatterns = [
    path("rub-to-usd/", RubRateAPIView.as_view(), name="rub-tu-usd")
]