from .models import *
from rest_framework import serializers
# from drf_writable_nested import WritableNestedModelSerializer


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['number', 'balance']

    def create(self, validated_data, **kwargs):

        number = validated_data.pop('number')
        wallet = Wallet.objects.create(**validated_data, number=number, balance=0)

        return wallet

    def validate(self, value):

        user_data = value['wallet']

        if self.instance:
            if (user_data['number'] != self.instance.number
                    or user_data['amount'] < self.instance.balance
                    or user_data['amount'] < 0):
                raise serializers.ValidationError()

        return value


class OperationSerializer(serializers.Serializer):
        operation_type = serializers.ChoiceField(choices=['DEPOSIT', 'WITHDRAW'])
        amount = serializers.FloatField(max_digits=10)
