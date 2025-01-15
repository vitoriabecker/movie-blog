# Generated by Django 3.2.23 on 2024-10-17 00:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_blog', '0007_auto_20241015_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['create_date']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 0, 13, 5, 317630, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 0, 13, 5, 317630, tzinfo=utc)),
        ),
    ]
