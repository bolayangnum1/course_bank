from rest_framework import serializers
from data.models import About, Bank, Contact


class AboutSerializers(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('title', 'text', 'img')


class BankSerializers(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ('address', 'info', 'big', 'iin', 'okpo')


class ContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('name', 'title', 'number_1', 'address')

