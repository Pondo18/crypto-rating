from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import crypto
from crypto.usecases import SearchCrypto


@csrf_exempt
def search_crypto(request):
    if request.method == 'POST':
        searched_crypto = request.POST['searched_crypto']
        use_case = SearchCrypto(searched_crypto.lower())
        try:
            combined_analysed_score = use_case.execute()
            crypto_data = {'name': searched_crypto, 'score': combined_analysed_score}
            return render(request, 'crypto/search_crypto.html', {'crypto_data': crypto_data})
        except crypto.models.Currencies.DoesNotExist:
            # messages.error(request, 'Crypto not found')
            return redirect('/')
