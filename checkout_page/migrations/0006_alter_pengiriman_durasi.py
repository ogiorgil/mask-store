# Generated by Django 3.2.7 on 2021-11-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout_page', '0005_alter_pengiriman_durasi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengiriman',
            name='durasi',
            field=models.CharField(choices=[('Next Day (1 hari)', 'Next Day (1 hari) *$3'), ('Reguler (2-4 hari)', 'Reguler (2-4 hari) *$1')], max_length=100),
        ),
    ]
