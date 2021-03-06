# Generated by Django 3.2.7 on 2021-10-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('telp', models.IntegerField()),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metode', models.CharField(choices=[('Mandiri', 'Mandiri Virtual Account'), ('BCA', 'BCA Virtual Account'), ('BankBCA', 'Bank BCA'), ('BankMANDIRI', 'Bank MANDIRI')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Pengiriman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durasi', models.CharField(choices=[(15000, 'Next Day (1 hari)'), (10000, 'Reguler (2-4 hari)')], max_length=2)),
                ('kurir', models.CharField(choices=[(13000, 'AnterAja'), (15000, 'Tiki'), (14000, 'JNE')], max_length=2)),
            ],
        ),
    ]
