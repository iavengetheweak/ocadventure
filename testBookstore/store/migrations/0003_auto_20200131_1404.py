# Generated by Django 2.2.7 on 2020-01-31 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200131_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
