# Generated by Django 5.0 on 2023-12-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='woman',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not published'), (1, 'Published')], default=1),
            preserve_default=False,
        ),
    ]