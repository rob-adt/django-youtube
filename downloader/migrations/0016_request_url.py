# Generated by Django 5.2.4 on 2025-07-23 10:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0015_remove_video_timereq_alter_request_timereq'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
