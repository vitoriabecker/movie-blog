# Generated by Django 3.2.23 on 2024-12-29 00:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_blog', '0027_auto_20241125_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 29, 0, 53, 22, 464766, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 29, 0, 53, 22, 464766, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
