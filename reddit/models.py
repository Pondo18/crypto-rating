from django.db import models

from crypto.models import Currencies


class Posts(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    text = models.CharField(max_length=5000)
    score = models.IntegerField()
    date = models.DateField()
    crypto_currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)


class SentimentScores(models.Model):
    post = models.OneToOneField(Posts, primary_key=True, on_delete=models.CASCADE)
    sentiment_score = models.FloatField()
