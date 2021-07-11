# Generated by Django 3.2 on 2021-07-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profit',
        ),
        migrations.AddField(
            model_name='item',
            name='total_in_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock_item',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='stock_total',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]