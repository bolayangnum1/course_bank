from rest_framework import generics
from account.models import Data, PhotoUser, Certificate, Pasport
from account.serializers import RegisterCreateSerializers, RegisterListSerializers, PhotoSerializers, \
    CertificateSerializers, PasportSerializers


class RegisterCreateView(generics.CreateAPIView):
    serializer_class = RegisterCreateSerializers
    queryset = Data.objects.all()
   # permission_classes = [IsAdminUser, ]


class RegisterListView(generics.ListAPIView):
    serializer_class = RegisterCreateSerializers
    queryset = Data.objects.all()
    #permission_classes = [IsAuthenticatedOrReadOnly, ]


class RegisterUpdateView(generics.UpdateAPIView):
    serializer_class = RegisterCreateSerializers
    queryset = Data.objects.all()
    #permission_classes = [IsAdminUser, ]


class RegisterDeleteView(generics.DestroyAPIView):
    serializer_class = RegisterCreateSerializers
    queryset = Data.objects.all()
    #permission_classes = [IsAdminUser, ]


class RegisterDetailID(generics.RetrieveAPIView):
    serializer_class = RegisterListSerializers
    queryset = Data.objects.all()
    #permission_classes = [IsAdminUser, ]


class CertificateListCreateView(generics.ListCreateAPIView):
    serializer_class = CertificateSerializers
    queryset = Certificate.objects.all()
  #  permission_classes = [IsAuthenticatedOrReadOnly, ]


class CertificateUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CertificateSerializers
    queryset = Certificate.objects.all()
   # permission_classes = [IsAdminUser, ]


class CertificateDetailID(generics.RetrieveAPIView):
    serializer_class = CertificateSerializers
    queryset = Certificate.objects.all()
    #permission_classes = [IsAdminUser, ]


class PasportListCreateView(generics.ListCreateAPIView):
    serializer_class = PasportSerializers
    queryset = Pasport.objects.all()
    #permission_classes = [IsAdminUser, ]


class PasportDetailID(generics.RetrieveAPIView):
    serializer_class = PasportSerializers
    queryset = Pasport.objects.all()
    #permission_classes = [IsAdminUser, ]


class PasportUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PasportSerializers
    queryset = Pasport.objects.all()
#    permission_classes = [IsAdminUser, ]


class PhotoUpdateView(generics.UpdateAPIView):
    serializer_class = PhotoSerializers
    queryset = PhotoUser.objects.all()
    #permission_classes = [IsAuthenticatedOrReadOnly, ]


class PhotoCreateView(generics.CreateAPIView):
    serializer_class = PhotoSerializers
    queryset = PhotoUser.objects.all()
    #permission_classes = [IsAuthenticatedOrReadOnly, ]


class PhotoDetailView(generics.RetrieveAPIView):
    serializer_class = PhotoSerializers
    queryset = PhotoUser.objects.all()
#    permission_classes = [IsAuthenticatedOrReadOnly, ]


class PhotoListView(generics.ListAPIView):
    serializer_class = PhotoSerializers
    queryset = PhotoUser.objects.all()
 #   permission_classes = [IsAdminUser, ]


class PhotoDeleteView(generics.DestroyAPIView):
    serializer_class = PhotoSerializers
    queryset = PhotoUser.objects.all()
 #   permission_classes = [IsAdminUser, ]
