# Generated by Django 5.0.6 on 2024-08-04 22:39

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('personal_data_agreement', models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
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
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
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
                ('directions', models.CharField(max_length=50, verbose_name='Направления')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'тренера',
                'verbose_name_plural': 'Тренерский состав',
            },
        ),
    ]
