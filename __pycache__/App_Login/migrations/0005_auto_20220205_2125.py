# Generated by Django 2.1 on 2022-02-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_auto_20220106_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
