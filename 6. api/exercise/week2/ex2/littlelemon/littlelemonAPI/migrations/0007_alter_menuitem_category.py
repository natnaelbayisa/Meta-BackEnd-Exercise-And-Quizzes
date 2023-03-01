# Generated by Django 4.1.7 on 2023-02-24 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonAPI', '0006_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='littlelemonAPI.category'),
        ),
    ]
