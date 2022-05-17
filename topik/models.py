from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField


User = get_user_model()


class TopicMain(models.Model):

    class Meta:
        verbose_name = "Тему"
        verbose_name_plural = "Темы"

    name = models.CharField('Название Темы', max_length=255, db_index=True)
    text = RichTextUploadingField('Описание темы')

    def __str__(self):
        return self.name


class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='пользователь')
    name_work = models.CharField('Название подтемы', max_length=255, db_index=True)
    name_topic = RichTextUploadingField('Описание подтемы', max_length=255, blank=True)

    class Meta:
        verbose_name = "Подтема"
        verbose_name_plural = "Подтемы"

    def __str__(self):
        return self.name_work


class File(models.Model):
    topik = models.ForeignKey(Topic, on_delete=models.PROTECT, verbose_name='Темы', related_name='files')
    title = models.CharField('Описание Файла', max_length=255)
    file = models.FileField('файл')

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return f'{self.topik}'


class Video(models.Model):
    topik = models.ForeignKey(Topic, on_delete=models.PROTECT, verbose_name='Подтема', related_name='videos')
    title = models.CharField('Описание видео', max_length=255)
    url = models.CharField('введите URL (Video)', blank=True, max_length=255)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return f'{self.topik}'


class ChoiceTopic(models.Model):
    topics = models.ForeignKey(Topic, on_delete=models.PROTECT, verbose_name='Подтема', related_name='topics_choice')
    topicmain = models.ForeignKey(TopicMain, on_delete=models.PROTECT, verbose_name='Темы', related_name='choice_topic')

    class Meta:
        verbose_name = "Выберите тему"
        verbose_name_plural = "Выберите темы"

    def __str__(self):
        return f'{self.topics}'