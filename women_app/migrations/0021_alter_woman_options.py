# Generated by Django 5.0 on 2024-01-04 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0020_alter_woman_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woman',
            options={'default_manager_name': 'published', 'get_latest_by': 'time_created', 'verbose_name': 'Woman', 'verbose_name_plural': 'Women'},
        ),
    ]
