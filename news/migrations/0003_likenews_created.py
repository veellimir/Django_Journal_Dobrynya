# Generated by Django 5.1.1 on 2024-09-10 11:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_likenews'),
    ]

    operations = [
        migrations.AddField(
            model_name='likenews',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]