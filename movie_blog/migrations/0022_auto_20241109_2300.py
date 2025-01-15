# Generated by Django 3.2.23 on 2024-11-10 02:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_blog', '0021_auto_20241109_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 10, 2, 0, 17, 937606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 10, 2, 0, 17, 937606, tzinfo=utc)),
        ),
    ]
