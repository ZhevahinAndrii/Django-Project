# Generated by Django 5.0 on 2023-12-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='woman',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
