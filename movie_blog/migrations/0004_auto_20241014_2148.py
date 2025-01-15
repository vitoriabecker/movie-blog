# Generated by Django 3.2.23 on 2024-10-15 00:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_blog', '0003_auto_20240508_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 15, 0, 48, 2, 817170, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2024, 10, 15, 0, 48, 2, 817170, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movie_blog.movie')),
            ],
        ),
    ]