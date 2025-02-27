# Generated by Django 5.0.6 on 2024-06-26 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='load',
            old_name='COMMODITY',
            new_name='commodity',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='CONTACT',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='DELIVERY_CITY_STATE',
            new_name='delivery_city_state',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='DELIVERY_DATE',
            new_name='delivery_date',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='FTL_LTL',
            new_name='ftl_ltl',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='LENGTH',
            new_name='length',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='LOAD_DESCRIPTION',
            new_name='load_description',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='NAME',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='PICKUP_CITY_STATE',
            new_name='pickup_city_state',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='PICKUP_DATE',
            new_name='pickup_date',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='PRICE',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='REFERENCE_LOAD_NUMBER',
            new_name='reference_load_number',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='TYPE',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='WEIGHT',
            new_name='weight',
        ),
    ]
