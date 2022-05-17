from rest_framework import generics

from course.views import IsPaid
from .serializers import *


class TestCreateView(generics.CreateAPIView):
    serializer_class = TestCreateSerializers
    queryset = Test.objects.all()


class TestListView(generics.ListAPIView):
    serializer_class = TestListSerializers
    queryset = Test.objects.all()


class TestUpdateView(generics.UpdateAPIView):
    serializer_class = TestCreateSerializers
    queryset = Test.objects.all()


class TestDeleteView(generics.DestroyAPIView):
    serializer_class = TestCreateSerializers
    queryset = Test.objects.all()


class TestDetailID(generics.RetrieveAPIView):
    serializer_class = TestListSerializers
    queryset = Test.objects.all()


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionCreateSerializers
    queryset = Question.objects.all()


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializers
    queryset = Question.objects.all()


class QuestionDeleteView(generics.DestroyAPIView):
    serializer_class = QuestionDeleteSerializers
    queryset = Question.objects.all()


class QuestionUpdateView(generics.UpdateAPIView):
    serializer_class = QuestionUpdateSerializers
    queryset = Question.objects.all()


class QuestionDetailIDVIew(generics.RetrieveAPIView):
    serializer_class = QuestionListSerializers
    queryset = Question.objects.all()
