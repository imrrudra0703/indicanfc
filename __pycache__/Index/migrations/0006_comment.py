# Generated by Django 2.1 on 2022-04-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0005_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]