from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def test(request, company_name):
    print(company_name)
    return HttpResponse("Working")

