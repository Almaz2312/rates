from django.urls import path

from rates.views import RubRateAPIView


urlpatterns = [
    path("get-current-usd/", RubRateAPIView.as_view(), name="get-current-usd")
]
