# Generated by Django 5.0 on 2023-12-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0006_remove_woman_women_app_w_slug_629e2c_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='woman',
            index=models.Index(fields=['slug'], name='women_app_w_slug_629e2c_idx'),
        ),
        migrations.AddIndex(
            model_name='womancategory',
            index=models.Index(fields=['slug'], name='women_app_w_slug_6a0a22_idx'),
        ),
    ]
