# Generated by Django 3.2.6 on 2021-08-27 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='Contract_spec',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='truck',
            name='material_spec',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='truck',
            name='plate_number',
            field=models.CharField(max_length=10),
        ),
    ]
