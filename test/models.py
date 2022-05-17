from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


class Question(models.Model):
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    title = models.CharField('Введите ваш вопрос|необязательно', max_length=255, blank=True, db_index=True, unique=True)
    img = CloudinaryField('Картинка|необязательно', blank=True, null=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name='необязательно')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Flag(models.Model):
    text = models.CharField('введите варианты ответов', max_length=255)
    boo = models.BooleanField('', default=False)
    test = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='Вопросы', related_name='flags')

    class Meta:
        verbose_name = "флажок"
        verbose_name_plural = "флажки"


class Test(models.Model):

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField('введите название теста', max_length=255, db_index=True, unique=True)
    text = RichTextUploadingField('введите текст', blank=True)
    timer = models.IntegerField('Введите длительность тестирования в минутах', blank=True)

    def __str__(self):
        return self.name


class СhoiceQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='Вопросы')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест', related_name='choicetest')

    class Meta:
        verbose_name = "Выберите вопрос"
        verbose_name_plural = "Выберите вопросы"