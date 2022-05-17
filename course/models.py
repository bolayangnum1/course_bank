from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from course.services import ACADEMICTIME
from topik.models import ChoiceTopic
from test.models import Test


User = get_user_model()


class Course(models.Model):
    title = models.CharField('Название курса', max_length=255, db_index=True)
    text = RichTextUploadingField('Введите описание')
    img = CloudinaryField('Файл png.', blank=True)
    types = models.CharField('Академическoe время', choices=ACADEMICTIME, max_length=50)
    price = models.DecimalField('Введите стоимость покупки курса', max_digits=12, decimal_places=2)
    time_work = models.IntegerField('Длительность', default=7)
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Начало курса')
    published_date = models.DateTimeField(blank=True, verbose_name='Завершение курса')
    test = models.ForeignKey(Test, on_delete=models.PROTECT, verbose_name='Тест')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ('title',)


class ChoiceTopicCourse(models.Model):
    choicetopic = models.ForeignKey(ChoiceTopic, on_delete=models.PROTECT, verbose_name='Темы', related_name='topicchoice')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='Курсы', related_name='coursechoice')

    class Meta:
        verbose_name = "Выберите тему"
        verbose_name_plural = "Выберите темы"

    def __str__(self):
        return f'{self.choicetopic}'


class TextCourse(models.Model):
    text = models.TextField('Введите описание')
    cou = models.ForeignKey(Course, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Описание курса"
        verbose_name_plural = "Описание курсов"

    def __str__(self):
        return self.text


class Scoreboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Пройден')
    score = models.PositiveIntegerField(default=0, verbose_name='Баллы')
    point = models.IntegerField(default=0, verbose_name='Правильные ответы')
    fail = models.IntegerField(default=0, verbose_name='неправильные ответы')
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата сдачи теста')
    quiz_room = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')

    class Meta:
        verbose_name = "Итог теста"
        verbose_name_plural = "Итоги тестов"

    def __str__(self):
        return f'{self.user}'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    subscription = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='Активен')
    active = models.BooleanField('подписан', default=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата активации')

    class Meta:
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курсы"

    def __str__(self):
        return f'{self.user}'


class ApplicationToAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    applicationcourse = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='В ожидании активации курса', related_name='application_detail')
    activation = models.BooleanField('Подтвердите активацию', default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата заявки')

    class Meta:
        verbose_name = "В ожидании активации курса"
        verbose_name_plural = "В ожидании активации курсов"
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.user}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, update_fields=update_fields, using=using)
        if self.activation:
            Subscription(user=self.user, subscription=self.applicationcourse).save()
