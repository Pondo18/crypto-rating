from django.shortcuts import render

from crypto.usecases import SearchCrypto


def search_crypto(request):
    if request.method == 'POST':
        searched_crypto = request.POST['searched_crypto']
        use_case = SearchCrypto(searched_crypto)
        combined_analysed_score = use_case.execute()
        crypto_data = {'name': searched_crypto, 'score': combined_analysed_score}
        return render(request, 'crypto/search_crypto.html', {'crypto_data': crypto_data})
