from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from course.models import *
from datetime import datetime


class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not phone_number:
            raise ValueError('Users must have a phone_number')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password=None):
        user = self.create_user(
            email=email,
            name=name,
            password=password,
            phone_number=phone_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = "Пользователь";
        verbose_name_plural = "Пользователи";

    name = models.CharField(max_length=125, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_admin = models.BooleanField(default=False, verbose_name='Админ')
    created_date = models.DateField(default=datetime.now, verbose_name='Дата создания')
    updated_date = models.DateField(default=datetime.now, verbose_name='Обновленная дата')
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь', blank=True)
    organization = models.CharField('Организация', max_length=100, blank=True)
    position = models.CharField('Должность', max_length=100, blank=True)

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"


class PhotoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    img = CloudinaryField('Фото')

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Pasport(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='пользователь')
    pasport_1 = CloudinaryField('фотография паспорта')
    pasport_2 = CloudinaryField('Заявление')

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорты"


class Certificate(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='пользователь')
    certificate_1 = CloudinaryField('место для сертификатов|RU', blank=True)
    certificate_2 = CloudinaryField('место для сертификатов|KG', blank=True)
    number_certificate = models.CharField('номер сертификата', blank=True, unique=True, max_length=20)

    class Meta:
        verbose_name = "сертификат"
        verbose_name_plural = "сертификаты"

    def __int__(self):
        return self.number_certificate
