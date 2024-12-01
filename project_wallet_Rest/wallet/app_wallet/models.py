from django.db import models


class Wallet(models.Model):
    """Wallet account"""

    number = models.IntegerField(max_length=10, verbose_name='Счет', unique=True)
    balance = models.FloatField(max_length=255, verbose_name='Баланс')

    def __str__(self):
        return f'Счет: {self.number}, баланс: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        self.save()
