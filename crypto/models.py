from django.db import models
import datetime


class Currency(models.Model):
    symbol = models.CharField(max_length=4, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    rank = models.IntegerField()
    active_top = models.BooleanField(default=True)
    last_changed = models.DateField(default=datetime.date.today)
