# Generated by Django 3.0.5 on 2020-04-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20200416_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='heading',
            field=models.CharField(default='Review', max_length=20),
            preserve_default=False,
        ),
    ]