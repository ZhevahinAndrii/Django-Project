# Generated by Django 5.0 on 2023-12-29 17:02

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0014_alter_woman_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woman',
            options={'base_manager_name': 'published', 'verbose_name': 'Woman', 'verbose_name_plural': 'Women'},
        ),
        migrations.AlterModelManagers(
            name='woman',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
