from rest_framework import serializers
from test.serializers import TestListSerializers
from topik.serializers import ChoiceTopicSerializer
from .models import Course, ChoiceTopicCourse, Scoreboard, Subscription, ApplicationToAdmin


class ChoiceTopicCourseSerializer(serializers.ModelSerializer):
    choicetopic = ChoiceTopicSerializer()

    class Meta:
        model = ChoiceTopicCourse
        fields = '__all__'


class CoursesDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    coursechoice = ChoiceTopicCourseSerializer(many=True)
    test = TestListSerializers()

    class Meta:
        model = Course
        fields = '__all__'


class CoursesCreateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ('user', 'id', 'title', 'text', 'img', 'types', 'price', 'time_work', 'created_date', 'published_date')


class CoursesListSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ('id', 'user', 'title', 'text', 'img', 'types', 'price', 'time_work', 'created_date', 'published_date')


class CoursesUpdateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ('user', 'id', 'title', 'text', 'img', 'types', 'price', 'time_work', 'created_date', 'published_date')


class CoursesDeleteSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ('user', 'id', 'title', 'text', 'img', 'types', 'price', 'time_work', 'created_date', 'published_date')


class ScoreboardCreateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scoreboard
        fields = '__all__'


class ScoreboardUpdateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scoreboard
        fields = '__all__'


class ScoreboardDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scoreboard
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class ApplicationToAdminSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ApplicationToAdmin
        fields = '__all__'


