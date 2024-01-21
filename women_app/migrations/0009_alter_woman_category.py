# Generated by Django 5.0 on 2023-12-29 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0008_woman_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='women_app', related_query_name='woman', to='women_app.womancategory'),
        ),
    ]
