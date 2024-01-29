from django.db import models


class FxRate(models.Model):
    rate = models.CharField(max_length=24)
    date_of_query = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
