# Generated by Django 3.2.23 on 2024-11-10 02:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_blog', '0020_auto_20241106_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 10, 2, 0, 7, 92859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 10, 2, 0, 7, 88323, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='movie_blog.movie')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
