# Generated by Django 5.0 on 2024-01-21 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0042_woman_author_alter_woman_husband'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='tags',
            field=models.ManyToManyField(related_name='posts', related_query_name='post', to='women_app.posttag', verbose_name='Теги'),
        ),
    ]
