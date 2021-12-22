from django.shortcuts import render

from crypto.usecases import SearchCrypto


def search_crypto(request):
    if request.method == 'POST':
        searched_crypto = request.POST['searched_crypto']
        combined_analysed_score = _run_use_case(searched_crypto)
        print(combined_analysed_score)
        return render(request, 'crypto/search_crypto.html', {'searched_crypto': searched_crypto})


def _run_use_case(searched_crypto):
    use_case = SearchCrypto(searched_crypto)
    return use_case.execute()
