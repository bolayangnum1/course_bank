from rest_framework import generics

from course.views import IsPaid
from .serializers import *


class TopikCreateView(generics.CreateAPIView):
    serializer_class = TopikCreateSerializers
    queryset = Topic.objects.all()


class TopikListView(generics.ListAPIView):
    serializer_class = TopikListSerializers
    queryset = Topic.objects.all()


class TopikUpdateView(generics.UpdateAPIView):
    serializer_class = TopikUpdateSerializers
    queryset = Topic.objects.all()


class TopikDeleteView(generics.DestroyAPIView):
    serializer_class = TopikDeleteSerializers
    queryset = Topic.objects.all()


class TopikDetail(generics.RetrieveAPIView):
    serializer_class = TopikDetailSerializers
    queryset = Topic.objects.all()


class TopicMainDetailView(generics.RetrieveAPIView):
    serializer_class = TopicMainDetailSerializer
    queryset = TopicMain.objects.all()


class TopicMainCreateView(generics.CreateAPIView):
    serializer_class = TopicMainDetailSerializer
    queryset = TopicMain.objects.all()


class TopicMainListView(generics.ListAPIView):
    serializer_class = TopicMainDetailSerializer
    queryset = TopicMain.objects.all()


class TopicMainDeleteView(generics.DestroyAPIView):
    serializer_class = TopicMainDetailSerializer
    queryset = TopicMain.objects.all()


class TopicMainUpdateView(generics.UpdateAPIView):
    serializer_class = TopicMainDetailSerializer
    queryset = TopicMain.objects.all()


class ChoiceTopicSerializer(generics.RetrieveAPIView):
    serializer_class = ChoiceTopicSerializer
    queryset = ChoiceTopic.objects.all()
