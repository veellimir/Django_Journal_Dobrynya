# Generated by Django 5.1.1 on 2024-09-05 08:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from app.mainapp.base_mixins import StrMixin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDirections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Направление тренировки')),
            ],
            options={
                'verbose_name': 'направление тренировки',
                'verbose_name_plural': 'Направления тренировок',
            },
            bases=(StrMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProfileAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='Изображения профиля')),
                ('phone', models.CharField(blank=True, max_length=110, null=True, verbose_name='Номер телефона')),
                ('telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телеграм')),
                ('vk', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вконтакте')),
                ('name', models.CharField(max_length=20, verbose_name='Имя тренера')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия тренера')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество тренера')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('directions', models.ManyToManyField(to='users.trainingdirections', verbose_name='Направления')),
            ],
            options={
                'verbose_name': 'тренера',
                'verbose_name_plural': 'Тренерский состав',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='Изображения профиля')),
                ('phone', models.CharField(blank=True, max_length=110, null=True, verbose_name='Номер телефона')),
                ('telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телеграм')),
                ('vk', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вконтакте')),
                ('date_of_birth', models.DateField(help_text='*', verbose_name='Дата рождения')),
                ('address', models.TextField(help_text='*', verbose_name='Адрес')),
                ('fio_parents', models.TextField(help_text='*', verbose_name='ФИО родителей')),
                ('parents_place_work', models.TextField(blank=True, null=True, verbose_name='Место работы родителей')),
                ('educational_institution', models.TextField(help_text='*', verbose_name='Образовательное учреждение (школа, класс, ФИО классного руководителя, номер телефона)')),
                ('time_school', models.TextField(help_text='*', verbose_name='Время начала и окончания учебных занятий в школе')),
                ('outside_club', models.TextField(help_text='*', verbose_name='Дополнительные занятия вне клуба (кружки, секции); время')),
                ('hobby', models.TextField(help_text='*', verbose_name='Хобби и увлечения')),
                ('sports', models.TextField(help_text='*', verbose_name='Виды спорта больше всего нравятся ребёнку')),
                ('about_club', models.TextField(help_text='*', verbose_name='Откуда узнали про клуб')),
                ('goals_season', models.TextField(help_text='*', verbose_name='Цели на сезон')),
                ('participation_competition', models.CharField(choices=[('yes', 'Да'), ('no', 'Нет')], help_text='*', max_length=3, verbose_name='Участие в соревнованиях')),
                ('wishes', models.TextField(blank=True, null=True, verbose_name='Пожелания')),
                ('points', models.PositiveIntegerField(default=3, verbose_name='Кол-во баллов профиля')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('directions', models.ManyToManyField(to='users.trainingdirections', verbose_name='Направления')),
            ],
            options={
                'verbose_name': 'дружинника',
                'verbose_name_plural': 'Вся дружина',
            },
        ),
    ]