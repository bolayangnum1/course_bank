# Generated by Django 3.2.8 on 2022-05-14 09:11

import ckeditor_uploader.fields
import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, unique=True, verbose_name='Введите ваш вопрос|необязательно')),
                ('img', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Картинка|необязательно')),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='необязательно')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='введите название теста')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='введите текст')),
                ('timer', models.IntegerField(blank=True, verbose_name='Введите длительность тестирования в минутах')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='СhoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test.question', verbose_name='Вопросы')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='choicetest', to='test.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Выберите вопрос',
                'verbose_name_plural': 'Выберите вопросы',
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='введите варианты ответов')),
                ('boo', models.BooleanField(default=False, verbose_name='')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flags', to='test.question', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'флажок',
                'verbose_name_plural': 'флажки',
            },
        ),
    ]
