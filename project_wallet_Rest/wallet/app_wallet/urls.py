from django.urls import path, include
from rest_framework import routers

from .views import WalletDetailView, WalletOperationView


urlpatterns = [
    path('wallets/<uuid:wallet_id>/operation', WalletOperationView.as_view(), name='wallet-operation'),
    path('wallets/<uuid:wallet_id>', WalletDetailView.as_view(), name='wallet-detail'),
]
