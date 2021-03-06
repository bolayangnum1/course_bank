# Generated by Django 3.2.8 on 2022-05-14 09:11

import ckeditor_uploader.fields
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
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='введите название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='введите текст')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='ставьте фотографию|необязательно')),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('info', models.CharField(max_length=20, verbose_name='Расчетный счет')),
                ('big', models.CharField(max_length=10, verbose_name='БИК')),
                ('iin', models.CharField(max_length=20, verbose_name='ИНН')),
                ('okpo', models.CharField(max_length=10, verbose_name='ОКПО')),
            ],
            options={
                'verbose_name': 'реквизит',
                'verbose_name_plural': 'реквизиты',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='наименование организации')),
                ('title', models.CharField(max_length=100, verbose_name='электронная почта')),
                ('number_1', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='номер телефона')),
                ('address', ckeditor_uploader.fields.RichTextUploadingField(max_length=100, verbose_name='Адрес')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
