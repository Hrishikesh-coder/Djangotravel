# Generated by Django 3.0.5 on 2020-04-18 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0009_auto_20200418_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='arriveson',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='departson',
        ),
    ]
