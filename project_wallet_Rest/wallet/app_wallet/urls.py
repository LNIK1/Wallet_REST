from django.urls import path, include
from rest_framework import routers

from .views import WalletCreateViewset, WalletDetailView

create_wallet = routers.DefaultRouter()
create_wallet.register(r'', WalletCreateViewset)

# edit_wallet = routers.DefaultRouter()
# edit_wallet.register(r'', WalletCreateViewset)

urlpatterns = [
    path('wallets/create/', include(create_wallet.urls)),
    # path('wallets/edit/', include(edit_wallet.urls)),

    # path('wallets/<uuid:wallet_uuid>/operation', WalletOperationView.as_view(), name='wallet-operation'),
    # path('wallets/<uuid:wallet_uuid>', WalletDetailView.as_view(), name='wallet-detail'),
]
