# Generated by Django 3.1.2 on 2021-03-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_merge_20210319_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='distributor',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Distributor $$'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='distributormargin',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='ldp',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Landed Duty Paid'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='listprice',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='List price'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='marginonsell',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='markup',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='Markup (in %)'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='netsellprice',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Net Sell Price'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='onnetsell',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='$$ On Net Sell Price'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='overhead',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Overhead'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='price',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='1st Cost'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='printval',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Print'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='totalcost',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Total Cost'),
        ),
        migrations.AlterField(
            model_name='adddomesticrawitem',
            name='totallandedcost',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Total Landed Cost'),
        ),
    ]
