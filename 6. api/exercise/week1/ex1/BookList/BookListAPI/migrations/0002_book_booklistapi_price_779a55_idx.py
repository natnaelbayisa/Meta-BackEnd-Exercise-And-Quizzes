# Generated by Django 4.1.4 on 2023-02-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['price'], name='BookListAPI_price_779a55_idx'),
        ),
    ]
