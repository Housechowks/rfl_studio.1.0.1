# Generated by Django 3.2.6 on 2021-08-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0003_position_delivery_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='Delivery_Number',
            field=models.IntegerField(default=0),
        ),
    ]
