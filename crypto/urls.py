from django.urls import path
from . import views

urlpatterns = [
    path('search_crypto', views.search_crypto, name='search-crypto'),
]
