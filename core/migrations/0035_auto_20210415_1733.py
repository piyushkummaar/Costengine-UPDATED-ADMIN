# Generated by Django 2.2 on 2021-04-15 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_adddomesticsizeitem_domesticsizeproduct_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domesticsizeproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='domesticsizeproduct',
            name='region',
        ),
        migrations.RemoveField(
            model_name='domesticsizeproduct',
            name='subcatagory',
        ),
        migrations.RemoveField(
            model_name='domesticsizeproduct',
            name='subsubcategory',
        ),
        migrations.DeleteModel(
            name='AddDomesticSizeItem',
        ),
        migrations.DeleteModel(
            name='DomesticSizeProduct',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
