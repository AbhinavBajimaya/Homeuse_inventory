# Generated by Django 3.2 on 2021-06-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210606_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
    ]
