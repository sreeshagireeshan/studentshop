# Generated by Django 4.1 on 2022-09-12 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_sellerregistration_tb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerregistration_tb',
            name='filename',
        ),
    ]
