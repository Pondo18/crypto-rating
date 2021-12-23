import datetime

from crypto.models import Currencies, AnalysedScores


class SearchCrypto:
    def __init__(self, searched_crypto):
        self.searched_crypto = searched_crypto

    def execute(self):
        crypto_currency = Currencies.objects.get(slug__exact=self.searched_crypto)
        analysed_scores = AnalysedScores.objects.filter(crypto_currency__exact=crypto_currency)
        return self._compute_combined_sentiment_score(analysed_scores)

    @staticmethod
    def _compute_combined_sentiment_score(analysed_scores):
        analysed_score = 0
        for analysed_score_object in analysed_scores:
            date = analysed_score_object.date
            weight = 0.9 ** (datetime.date.today() - date).days
            analysed_score = (analysed_score + analysed_score_object.score * weight) / (1 + weight)
        return round(analysed_score, 2)
