# Generated by Django 3.0.5 on 2020-04-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_reviews_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='destination',
            field=models.CharField(default='Hrishikesh', max_length=200),
        ),
    ]