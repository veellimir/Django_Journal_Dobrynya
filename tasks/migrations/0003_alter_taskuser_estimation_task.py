# Generated by Django 5.0.6 on 2024-08-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_taskuser_description_taskuser_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskuser',
            name='estimation_task',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Оценка'),
        ),
    ]