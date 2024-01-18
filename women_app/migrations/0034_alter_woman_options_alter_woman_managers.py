# Generated by Django 5.0 on 2024-01-09 18:12

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0033_alter_woman_options_alter_womancategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woman',
            options={'default_manager_name': 'published', 'get_latest_by': 'time_created', 'verbose_name': 'Жінка', 'verbose_name_plural': 'Жінки'},
        ),
        migrations.AlterModelManagers(
            name='woman',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]