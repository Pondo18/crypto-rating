from django.shortcuts import render


def search_crypto(request):
    if request.method == 'POST':
        searched_crypto = request.POST['searched_crypto']

        return render(request, 'crypto/search_crypto.html', {'searched_crypto': searched_crypto})