from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


class WalletTest(APITestCase):

    def setUp(self):
        self.wallet = Wallet.objects.create(number='111')
        self.wallet_id = self.wallet.id
        self.wallet_number = self.wallet.number

    def test_deposit(self):
        url = reverse('wallet-operation', kwargs={'wallet_id': self.wallet_id})
        data = {
            "operationType": "DEPOSIT",
            "amount": '1000'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], '1000.00')

    def test_withdraw(self):

        self.wallet.balance = 1000
        self.wallet.save()

        url = reverse('wallet-operation', kwargs={'wallet_id': self.wallet_id})
        data = {
            "operationType": "WITHDRAW",
            "amount": "500"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], '500.00')

    def test_withdraw_not_enough(self):
        url = reverse('wallet-operation', kwargs={'wallet_id': self.wallet_id})
        data = {
            "operationType": "WITHDRAW",
            "amount": "500"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Недостаточно средств')

    def test_get_balance(self):
        url = reverse('wallet-detail', kwargs={'wallet_id': self.wallet_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], '0.00')

    def test_non_exist_wallet(self):
        url = reverse('wallet-detail', kwargs={'wallet_id': 'f0e00ebc-00ff-0f00-ab0f-00c00be0b0fb'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Кошелек не найден.')
