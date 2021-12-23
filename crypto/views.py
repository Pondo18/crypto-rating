from django.shortcuts import render

from crypto.usecases import SearchCrypto


def search_crypto(request):
    if request.method == 'POST':
        searched_crypto = request.POST['searched_crypto']
        use_case = SearchCrypto(searched_crypto)
        combined_analysed_score = use_case.execute()
        print(combined_analysed_score)
        return render(request, 'crypto/search_crypto.html', {'searched_crypto': searched_crypto})
