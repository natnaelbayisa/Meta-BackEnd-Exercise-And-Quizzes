# Generated by Django 4.1.7 on 2023-02-24 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonAPI', '0010_remove_menuitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='categori', to='littlelemonAPI.category'),
        ),
    ]
