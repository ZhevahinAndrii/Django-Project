# Generated by Django 5.0 on 2024-01-10 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0035_alter_woman_options_alter_woman_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woman',
            options={'get_latest_by': 'time_created', 'ordering': ('time_created',), 'verbose_name': 'Жінка', 'verbose_name_plural': 'Жінки'},
        ),
    ]
