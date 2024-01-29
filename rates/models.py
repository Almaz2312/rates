from django.db import models


# {
#   "RUB to USD rate": 0.0111,
#   "date": "2024-01-29"
# }

class FxRate(models.Model):
    rate = models.CharField(max_length=24)
    date_of_query = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
