# Generated by Django 2.1 on 2022-04-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0004_exhibition_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]