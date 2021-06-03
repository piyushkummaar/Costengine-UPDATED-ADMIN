# Generated by Django 2.1.15 on 2021-03-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210302_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddomesticitem',
            name='baseproductsalesprice',
            field=models.FloatField(blank=True, null=True, verbose_name='Base Product Sales Price C$'),
        ),
        migrations.AlterField(
            model_name='adddomesticitem',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adddomesticitem',
            name='productcost',
            field=models.FloatField(blank=True, null=True, verbose_name='Product Cost C$'),
        ),
    ]
