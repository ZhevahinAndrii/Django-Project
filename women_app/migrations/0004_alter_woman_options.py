# Generated by Django 5.0 on 2023-12-28 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0003_alter_woman_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woman',
            options={'verbose_name': 'Жінка', 'verbose_name_plural': 'Women'},
        ),
    ]