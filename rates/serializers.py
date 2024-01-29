from rest_framework import serializers

from rates.models import FxRate


class FxRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FxRate
        fields = "__all__"


class Final(serializers.Serializer):
    last_queries = FxRateSerializer(many=True)
    rate = serializers.CharField()
    date = serializers.DateField()