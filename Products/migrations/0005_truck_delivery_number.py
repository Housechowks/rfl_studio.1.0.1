# Generated by Django 3.2.6 on 2021-08-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_auto_20210827_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='Delivery_Number',
            field=models.IntegerField(default=[('', '---------')]),
        ),
    ]
