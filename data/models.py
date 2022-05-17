from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField


User = get_user_model()


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('наименование организации', max_length=50)
    title = models.CharField('электронная почта', max_length=100)
    number_1 = RichTextUploadingField('номер телефона')
    address = RichTextUploadingField('Адрес', max_length=100)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name


class Bank(models.Model):
    address = models.CharField('Адрес', max_length=200)
    info = models.CharField('Расчетный счет', max_length=20)
    big = models.CharField('БИК', max_length=10)
    iin = models.CharField('ИНН', max_length=20)
    okpo = models.CharField('ОКПО', max_length=10)

    class Meta:
        verbose_name = "реквизит"
        verbose_name_plural = "реквизиты"

    def __str__(self):
        return self.info


class About(models.Model):
    title = models.CharField('введите название', max_length=255,)
    text = RichTextUploadingField('введите текст')
    img = models.ImageField('ставьте фотографию|необязательно', blank=True, null=True)

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"

    def __str__(self):
        return self.title
