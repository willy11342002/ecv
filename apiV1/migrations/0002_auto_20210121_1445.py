# Generated by Django 3.0.8 on 2021-01-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiV1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='AvailabilityZone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='Operation',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='ResourceId',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='UsageType',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductName',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='cacheEngine',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='databaseEdition',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='databaseEngine',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='deploymentOption',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='instanceType',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='instanceTypeFamily',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='licenseModel',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='operatingSystem',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='region',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tenancy',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
