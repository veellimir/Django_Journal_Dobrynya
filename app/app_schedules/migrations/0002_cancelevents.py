# Generated by Django 5.1.2 on 2024-10-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_schedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelled_title', models.CharField(max_length=100, verbose_name='Название тренировки')),
                ('cancelled_date', models.DateTimeField(verbose_name='Дата отмены')),
                ('cancelled_red_color', models.CharField(default='#FF0000', max_length=7)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание отмены')),
            ],
        ),
    ]