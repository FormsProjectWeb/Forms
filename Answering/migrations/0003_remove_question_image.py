# Generated by Django 3.2.6 on 2024-04-17 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Answering', '0002_auto_20240416_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]
