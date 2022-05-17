from rest_framework import generics
from .serializers import AboutSerializers, BankSerializers,\
    ContactSerializers
from .models import About, Bank, Contact


class AboutListCreateView(generics.ListCreateAPIView):
    serializer_class = AboutSerializers
    queryset = About.objects.all()


class AboutUpdateDeleteView(generics.ListCreateAPIView):
    serializer_class = AboutSerializers
    queryset = About.objects.all()


class BankListView(generics.ListAPIView):
    serializer_class = BankSerializers
    queryset = Bank.objects.all()


class BankUpdateView(generics.UpdateAPIView):
    serializer_class = BankSerializers
    queryset = Bank.objects.all()


class BankCreateView(generics.CreateAPIView):
    serializer_class = BankSerializers
    queryset = Bank.objects.all()


class BankDeleteView(generics.DestroyAPIView):
    serializer_class = BankSerializers
    queryset = Bank.objects.all()


class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()


class ContactListView(generics.ListAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()


class ContactUpdateView(generics.UpdateAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()


class ContactDeleteView(generics.DestroyAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()


