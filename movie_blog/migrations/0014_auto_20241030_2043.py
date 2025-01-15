# Generated by Django 3.2.23 on 2024-10-30 23:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_blog', '0013_auto_20241029_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='image_extension',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='image_name',
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 30, 23, 43, 51, 928556, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 30, 23, 43, 51, 928556, tzinfo=utc)),
        ),
    ]