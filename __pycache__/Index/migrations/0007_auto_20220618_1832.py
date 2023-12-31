# Generated by Django 2.0 on 2022-06-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Open_Mic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('types', models.CharField(choices=[('A', 'English Poem'), ('B', 'Hindi Poem'), ('C', 'Shayari'), ('D', 'Story Telling'), ('E', 'Musical performance'), ('F', 'Regional poetry'), ('G', 'Other')], max_length=7)),
                ('content', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Query',
        ),
    ]
