# Generated by Django 5.2.4 on 2025-07-23 10:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0016_request_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='timereq',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
