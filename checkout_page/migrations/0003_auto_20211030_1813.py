# Generated by Django 3.1.5 on 2021-10-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout_page', '0002_auto_20211028_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembayaran',
            name='metode',
            field=models.CharField(choices=[('Mandiri Virtual Account', 'Mandiri Virtual Account'), ('BCA Virtual Account', 'BCA Virtual Account'), ('Bank BCA', 'Bank BCA'), ('Bank MANDIRI', 'Bank MANDIRI')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pengiriman',
            name='durasi',
            field=models.CharField(choices=[('Next Day (1 hari) *Rp 10.000', 'Next Day (1 hari) *Rp 10.000'), ('Reguler (2-4 hari) *Rp 15.000', 'Reguler (2-4 hari) *Rp 15.000')], max_length=100),
        ),
    ]
