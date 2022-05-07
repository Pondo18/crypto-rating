from django.db import models
import datetime


class Currencies(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    slug = models.CharField(max_length=32, unique=True)
    rank = models.IntegerField(null=True)
    active_top = models.BooleanField(auto_created=True)
    last_changed = models.DateField(auto_now_add=datetime.date.today())


class AnalysedScores(models.Model):
    date = models.DateField(auto_now_add=datetime.date.today(), primary_key=True)
    crypto_currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'crypto_analysed_scores'
        unique_together = (('date', 'crypto_currency'),)

