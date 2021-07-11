# Generated by Django 3.2 on 2021-07-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210711_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='owner_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sale_item',
            name='current',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sale_item',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale_item',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale_total',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]