# Generated by Django 3.0.5 on 2020-04-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart',
            field=models.IntegerField(default=0),
        ),
    ]
