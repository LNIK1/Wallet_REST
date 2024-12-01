from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import WalletSerializer, OperationSerializer


class WalletCreateViewset(viewsets.ModelViewSet):
    """Создание Wallet"""

    queryset = Wallet.objects.filter(id=0)
    serializer_class = WalletSerializer

    def create(self, request, *args, **kwargs):

        serializer = WalletSerializer(data=request.data)
        response_data = {}

        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 200,
                'message': '',
                'id': serializer.data.get('id')
            }

        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            response_data = {
                'status': 500,
                'message': 'Ошибка подключения к базе данных',
                'id': serializer.data.get('id')
            }

        elif status.HTTP_400_BAD_REQUEST:
            response_data = {
                'status': 400,
                'message': 'Неверный запрос',
                'id': serializer.data.get('id')
            }

        return Response(response_data)


class WalletOperationView(APIView):

    def post(self, request, wallet_uuid):
        try:
            wallet = Wallet.objects.get(uuid=wallet_uuid)
        except Wallet.DoesNotExist:
            return Response({"error": "Кошелька не существует."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operation_type = serializer.validated_data['operationType']
            amount = serializer.validated_data['amount']

            if operation_type == 'DEPOSIT':
                wallet.deposit(amount)
            elif operation_type == 'WITHDRAW':
                try:
                    wallet.withdraw(amount)
                except ValueError as e:
                    return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"balance": str(wallet.balance)}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletDetailView(APIView):
    def get(self, request, wallet_uuid):
        try:
            wallet = Wallet.objects.get(uuid=wallet_uuid)
        except Wallet.DoesNotExist:
            return Response({"error": "Кошелек не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer = WalletSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

