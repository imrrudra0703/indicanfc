# Generated by Django 2.1 on 2022-02-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_auto_20220113_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
