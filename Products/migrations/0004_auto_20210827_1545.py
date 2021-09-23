# Generated by Django 3.2.6 on 2021-08-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_truck_current_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='current_rates',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='destination',
            field=models.SmallIntegerField(default=1, help_text='K '),
        ),
    ]