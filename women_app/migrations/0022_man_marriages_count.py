# Generated by Django 5.0 on 2024-01-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0021_alter_woman_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='marriages_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
