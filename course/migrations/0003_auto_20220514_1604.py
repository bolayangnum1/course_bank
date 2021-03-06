# Generated by Django 3.2.8 on 2022-05-14 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_alter_course_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtoadmin',
            name='applicationcourse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='application_detail', to='course.course', verbose_name='В ожидании активации курса'),
        ),
        migrations.AlterField(
            model_name='applicationtoadmin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Пользователь'),
        ),
    ]
