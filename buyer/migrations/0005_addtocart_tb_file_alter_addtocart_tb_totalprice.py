# Generated by Django 4.1 on 2022-09-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_alter_addtocart_tb_totalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart_tb',
            name='file',
            field=models.FileField(default=1, upload_to=''),
        ),
        migrations.AlterField(
            model_name='addtocart_tb',
            name='totalprice',
            field=models.IntegerField(),
        ),
    ]
