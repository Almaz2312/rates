from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rates.tasks import get_currency_rates


class RubRateAPIView(generics.ListAPIView):
    queryset = None
    serializer_class = None
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        rates = get_currency_rates("RUB")
        rub_to_usd = rates.get("rates").get("USD")
        date = rates.get("date")
        return Response(data={"RUB to USD rate": rub_to_usd, "date": date}, status=status.HTTP_200_OK)
