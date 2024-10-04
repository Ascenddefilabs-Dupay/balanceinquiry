# Generated by Django 5.0.7 on 2024-10-04 05:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCMS',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('account_type', models.CharField(blank=True, max_length=100, null=True)),
                ('currency_type', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'admincms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FiatWallet',
            fields=[
                ('fiat_wallet_id', models.CharField(blank=True, max_length=12)),
                ('fiat_wallet_address', models.CharField(blank=True, max_length=255)),
                ('fiat_wallet_type', models.CharField(max_length=50)),
                ('fiat_wallet_currency', models.CharField(max_length=10)),
                ('fiat_wallet_balance', models.DecimalField(decimal_places=8, default=0, max_digits=18)),
                ('fiat_wallet_created_time', models.DateTimeField(auto_now_add=True)),
                ('fiat_wallet_updated_time', models.DateTimeField(auto_now=True)),
                ('fiat_wallet_phone_number', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Invalid phone number format.', regex='^\\+?1?\\d{9,15}$')])),
                ('fiat_wallet_email', models.EmailField(max_length=254)),
                ('user_id', models.CharField(max_length=255)),
                ('qr_code', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fiat_wallet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserCurrency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wallet_id', models.CharField(max_length=255)),
                ('currency_type', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=8, default=0, max_digits=18)),
            ],
            options={
                'db_table': 'user_currencies',
                'managed': False,
            },
        ),
    ]