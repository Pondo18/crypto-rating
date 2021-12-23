from django.shortcuts import render

from crypto.models import Currencies
from crypto.usecases import SearchCrypto


def index(request):
    crypto_currencies = Currencies.objects.filter()
    top_crypto = _get_top_crypto(crypto_currencies)
    return render(request, 'pages/index.html', {'top_crypto': top_crypto})


def _get_top_crypto(crypto_currencies):
    analysed_scores_for_all_crypto = []
    for crypto in crypto_currencies:
        use_case = SearchCrypto(crypto.slug)
        analysed_scores_for_all_crypto.append({'name': crypto.slug, 'score': use_case.execute()})
    return sorted(analysed_scores_for_all_crypto, key=lambda i: (i['score']), reverse=True)[:6]
