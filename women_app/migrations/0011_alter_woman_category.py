# Generated by Django 5.0 on 2023-12-29 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0010_alter_woman_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='women_app.womancategory'),
        ),
    ]