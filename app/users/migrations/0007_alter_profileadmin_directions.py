# Generated by Django 5.1.2 on 2025-02-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_administrationperson_alter_profileparent_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileadmin',
            name='directions',
            field=models.ManyToManyField(blank=True, to='users.trainingdirections', verbose_name='Направления'),
        ),
    ]
