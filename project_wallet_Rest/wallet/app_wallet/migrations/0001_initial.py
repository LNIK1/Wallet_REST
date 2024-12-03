# Generated by Django 5.1.3 on 2024-12-02 05:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('number', models.CharField(unique=True, verbose_name='Счет')),
                ('balance', models.FloatField(verbose_name='Баланс')),
            ],
        ),
    ]
