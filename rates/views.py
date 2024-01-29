from datetime import timedelta
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rates.models import FxRate
from rates.serializers import FxRateSerializer
from rates.tasks import get_currency_rates


class RubRateAPIView(generics.ListAPIView):
    queryset = FxRate.objects.all()
    serializer_class = FxRateSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        rate, date = get_currency_rates()
        last_queries = FxRate.objects.all().order_by("-created_date")[:10]
        data = FxRateSerializer(last_queries, many=True).data
        if not last_queries or timezone.now() - timedelta(seconds=10) > last_queries[0].created_date:
            FxRate.objects.create(rate=rate, date_of_query=date)
            return Response(data={"RUB to USD rate": rate, "date": date, "last_queries": data}, status=status.HTTP_200_OK)

        return Response(data={"RUB to USD rate": rate, "date": date, "last_queries": data}, status=status.HTTP_200_OK)
