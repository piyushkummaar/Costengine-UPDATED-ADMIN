# Generated by Django 2.2 on 2021-04-13 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20210322_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomesticSizeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=250, unique=True)),
                ('productname', models.CharField(max_length=250)),
                ('markup', models.IntegerField(blank=True, default=35, null=True, verbose_name='Mark Up Rate(in %)')),
                ('productcostc', models.FloatField(blank=True, default=0.494, null=True, verbose_name='Product Cost C$')),
                ('targetgrossprofit', models.IntegerField(blank=True, default=33, null=True, verbose_name='Target Gross Profit (in %)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region')),
                ('subcatagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubCategory')),
                ('subsubcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubSubCategory')),
            ],
            options={
                'verbose_name': 'Domestic(Size) Product',
                'verbose_name_plural': 'Domestic(Size) Products',
                'db_table': 'tbl_domesticsizeproducts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AddDomesticSizeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('productcost', models.FloatField(blank=True, null=True, verbose_name='Product Cost C$')),
                ('baseproductsalesprice', models.FloatField(blank=True, null=True, verbose_name='Base Product Sales Price C$')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DomesticSizeProduct')),
            ],
            options={
                'verbose_name': 'Domestic Item',
                'verbose_name_plural': 'Domestic Items',
                'db_table': 'tbl_domesticsizeitems',
                'managed': True,
            },
        ),
    ]