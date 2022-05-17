from rest_framework import generics
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Course, Scoreboard, Subscription, ApplicationToAdmin, ChoiceTopicCourse
from .serializers import CoursesListSerializers, CoursesCreateSerializers, CoursesUpdateSerializers, \
    CoursesDeleteSerializers, CoursesDetailSerializers, ScoreboardCreateListSerializer, ApplicationToAdminSerializer, \
    ChoiceTopicCourseSerializer, SubscriptionSerializer


class IsPaid(BasePermission):
    def has_permission(self, request, view, *args, **kwargs):
        course_id = request.resolver_match.kwargs.get('course_id')
        subs = Subscription.objects.filter(user=request.user, subscription=course_id).first()
        return bool(subs)


class CoursesCreateView(generics.CreateAPIView):
    serializer_class = CoursesCreateSerializers
    queryset = Course.objects.all()


class CoursesListView(generics.ListAPIView):
    serializer_class = CoursesListSerializers
    queryset = Course.objects.all()


class CoursesUpdateView(generics.UpdateAPIView):
    serializer_class = CoursesUpdateSerializers
    queryset = Course.objects.all()


class CoursesDeleteView(generics.DestroyAPIView):
    serializer_class = CoursesDeleteSerializers
    queryset = Course.objects.all()


class CourseDetail(generics.RetrieveAPIView):
    serializer_class = CoursesDetailSerializers
    queryset = Course.objects.all()


class ScoreboardCreateListView(generics.ListCreateAPIView):
    serializer_class = ScoreboardCreateListSerializer
    queryset = Scoreboard.objects.all()


class ScoreboardDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScoreboardCreateListSerializer
    queryset = Scoreboard.objects.all()


class ScoreboardDetailView(generics.RetrieveAPIView):
    serializer_class = ScoreboardCreateListSerializer
    queryset = Scoreboard.objects.all()


class SubscriptionCreate(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionList(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionUpdate(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionDelete(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionDetail(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class ApplicationToAdminCreate(generics.CreateAPIView):
    serializer_class = ApplicationToAdminSerializer
    queryset = ApplicationToAdmin.objects.all()


class ApplicationToAdminList(generics.ListAPIView):
    serializer_class = ApplicationToAdminSerializer
    queryset = ApplicationToAdmin.objects.all()


class ApplicationToAdminUpdate(generics.UpdateAPIView):
    serializer_class = ApplicationToAdminSerializer
    queryset = ApplicationToAdmin.objects.all()


class ApplicationToAdminDelete(generics.DestroyAPIView):
    serializer_class = ApplicationToAdminSerializer
    queryset = ApplicationToAdmin.objects.all()


class ApplicationToAdminDetail(generics.RetrieveAPIView):
    serializer_class = ApplicationToAdminSerializer
    queryset = ApplicationToAdmin.objects.all()


class ChoiceTopicCourseSerializer(generics.RetrieveAPIView):
    serializer_class = ChoiceTopicCourseSerializer
    queryset = ChoiceTopicCourse.objects.all()


class IndexAPIview(APIView):
    permission_classes = [IsPaid]

    def get(self, request, course_id):
        return HttpResponse(f"<h1> Welcome! <h1>")