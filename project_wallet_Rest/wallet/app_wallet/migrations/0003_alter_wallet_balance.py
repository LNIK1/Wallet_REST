# Generated by Django 5.1.3 on 2024-12-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_wallet', '0002_alter_wallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='Баланс'),
        ),
    ]
