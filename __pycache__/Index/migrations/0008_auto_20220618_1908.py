# Generated by Django 3.1.1 on 2022-06-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0007_auto_20220618_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open_mic',
            name='types',
            field=models.CharField(max_length=50),
        ),
    ]
