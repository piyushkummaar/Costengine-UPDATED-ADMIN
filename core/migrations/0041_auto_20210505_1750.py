# Generated by Django 2.2 on 2021-05-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20210505_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domesticproductraw',
            name='fleece',
            field=models.FloatField(blank=True, null=True, verbose_name='fleece(in %)'),
        ),
        migrations.AlterField(
            model_name='domesticproductraw',
            name='sewing',
            field=models.FloatField(blank=True, null=True, verbose_name='sewing(in %)'),
        ),
    ]
