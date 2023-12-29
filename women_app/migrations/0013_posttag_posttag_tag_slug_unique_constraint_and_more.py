# Generated by Django 5.0 on 2023-12-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0012_alter_woman_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.AddConstraint(
            model_name='posttag',
            constraint=models.UniqueConstraint(fields=('slug',), name='tag_slug_unique_constraint'),
        ),
        migrations.AddField(
            model_name='woman',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='women_app.posttag'),
        ),
    ]
