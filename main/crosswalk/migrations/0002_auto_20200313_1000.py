# Generated by Django 3.0.3 on 2020-03-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosswalk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalelement',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='externalrelationshipschema',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]