# Generated by Django 5.0 on 2024-01-09 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0031_alter_woman_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woman',
            options={'default_manager_name': 'published', 'get_latest_by': 'time_created', 'verbose_name': 'Жінка', 'verbose_name_plural': 'Жінки'},
        ),
    ]