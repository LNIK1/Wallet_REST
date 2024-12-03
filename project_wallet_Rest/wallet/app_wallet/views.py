from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import WalletSerializer, OperationSerializer


class WalletOperationView(APIView):

    def post(self, request, wallet_id):
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response({"detail": "Кошелек не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operation_type = serializer.validated_data['operationType']
            amount = serializer.validated_data['amount']

            if operation_type not in ['DEPOSIT', 'WITHDRAW']:
                return Response({"detail": "Некорректный тип операции"}, status=status.HTTP_400_BAD_REQUEST)

            if amount <= 0:
                return Response({"detail": "Сумма должна быть больше 0"}, status=status.HTTP_400_BAD_REQUEST)

            if operation_type == 'DEPOSIT':
                wallet.deposit(amount)
            elif operation_type == 'WITHDRAW':
                try:
                    wallet.withdraw(amount)
                except ValueError as e:
                    return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"wallet": wallet.number, "balance": str(wallet.balance)}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletDetailView(APIView):
    def get(self, request, wallet_id):
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response({"detail": "Кошелек не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer = WalletSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

