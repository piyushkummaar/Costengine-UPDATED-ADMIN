# Generated by Django 2.1.15 on 2021-02-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_adddomesticrawitem_totalcost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domesticproductraw',
            name='ldp',
        ),
        migrations.RemoveField(
            model_name='domesticproductraw',
            name='printval',
        ),
        migrations.RemoveField(
            model_name='domesticproductraw',
            name='productcostc',
        ),
        migrations.RemoveField(
            model_name='domesticproductraw',
            name='targetgrossprofit',
        ),
        migrations.RemoveField(
            model_name='domesticproductraw',
            name='totalcost',
        ),
        migrations.AddField(
            model_name='domesticproductraw',
            name='broker',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Duty(in %)'),
        ),
        migrations.AddField(
            model_name='domesticproductraw',
            name='duty',
            field=models.IntegerField(blank=True, default=18, null=True, verbose_name='Duty(in %)'),
        ),
        migrations.AddField(
            model_name='domesticproductraw',
            name='exchage',
            field=models.IntegerField(blank=True, default=35, null=True, verbose_name='Exchange(in %)'),
        ),
        migrations.AddField(
            model_name='domesticproductraw',
            name='freight',
            field=models.IntegerField(blank=True, default=10, null=True, verbose_name='Freight(in %)'),
        ),
        migrations.AlterField(
            model_name='domesticproductraw',
            name='overhead',
            field=models.DecimalField(blank=True, decimal_places=2, default=33, max_digits=5, null=True, verbose_name='Overhead(in %)'),
        ),
    ]
