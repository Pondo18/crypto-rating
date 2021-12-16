from django.db import models

from crypto.models import Currency


class Posts(models.Model):
    text = models.CharField(max_length=300)
    score = models.IntegerField()
    date = models.DateField()
    crypto_currency = models.OneToOneField(Currency, on_delete=models.CASCADE)


class SentimentScores(models.Model):
    post = models.OneToOneField(Posts, primary_key=True, on_delete=models.CASCADE)
    sentiment_score = models.FloatField()
