from django.contrib.auth import authenticate, get_user_model
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers

from account.models import Data, PhotoUser, Pasport, Certificate

User = get_user_model()


class RegisterCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id', 'user', 'position', 'organization')


class RegisterListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id', 'user', 'position', 'organization')


class RegisterUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id', 'user', 'position', 'organization')


class RegisterDeleteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id', 'user', 'position', 'organization')


class PhotoSerializers(serializers.ModelSerializer):

    class Meta:
        model = PhotoUser
        fields = ('id', 'user', 'img')


class CustomTokenCreateSerializer(TokenCreateSerializer):
    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user:
            return attrs
        self.fail("invalid_credentials")


class PasportSerializers(serializers.ModelSerializer):

    class Meta:
        model = Pasport
        fields = ('id', 'user', 'pasport_1', 'pasport_2')


class CertificateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('id', 'user', 'certificate_1', 'certificate_2', 'number_certificate')

