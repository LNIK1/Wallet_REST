import uuid

from django.db import models


class Wallet(models.Model):
    """Wallet account"""

    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    number = models.CharField(verbose_name='Счет', unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Баланс', default=0.00)

    def __str__(self):
        return f'uuid: {self.id}, Счет: {self.number}, баланс: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        self.save()
