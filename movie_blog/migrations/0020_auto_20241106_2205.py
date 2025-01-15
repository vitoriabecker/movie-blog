# Generated by Django 3.2.23 on 2024-11-07 01:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_blog', '0019_auto_20241106_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 7, 1, 5, 31, 971289, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 7, 1, 5, 31, 971289, tzinfo=utc)),
        ),
    ]
