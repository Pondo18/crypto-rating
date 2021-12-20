from django.db import models
import datetime


class Currencies(models.Model):
    symbol = models.CharField(max_length=5, unique=True)
    slug = models.CharField(max_length=32, unique=True)
    rank = models.IntegerField(null=True)
    active_top = models.BooleanField(auto_created=True)
    last_changed = models.DateField(auto_now_add=datetime.date.today())
