# Generated by Django 3.2.7 on 2021-10-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuztomize_masker_page', '0007_auto_20211028_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='custommask',
            name='color',
            field=models.CharField(choices=[('RED', 'Red'), ('GREEN', 'Green'), ('BLUE', 'Blue'), ('BLACK', 'Black')], default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='custommask',
            name='model',
            field=models.CharField(choices=[('SURGICAL', 'Surgical'), ('SPONGE', 'Sponge'), ('PITTA', 'Pitta'), ('CLOTH', 'Cloth')], default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='custommask',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unisex')], default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='custommask',
            name='size',
            field=models.CharField(choices=[('XL', 'Extra Large'), ('L', 'Large'), ('M', 'Medium'), ('S', 'Small')], default=None, max_length=8),
        ),
    ]
