# Generated by Django 3.1.1 on 2022-10-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0008_auto_20220618_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
