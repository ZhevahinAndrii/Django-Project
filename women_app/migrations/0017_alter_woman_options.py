# Generated by Django 5.0 on 2023-12-29 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0016_alter_woman_options_alter_woman_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woman',
            options={'default_manager_name': 'published', 'verbose_name': 'Woman', 'verbose_name_plural': 'Women'},
        ),
    ]
