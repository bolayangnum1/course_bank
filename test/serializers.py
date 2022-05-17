from .models import *
from rest_framework import serializers
from django.utils import timezone


class TestCreateSerializers(serializers.ModelSerializer):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)

    class Meta:
        model = Test
        fields = '__all__'


class FlagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flag
        fields = '__all__'


class QuestionSerializers(serializers.ModelSerializer):
    flags = FlagSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class СhoiceQuestionSerializers(serializers.ModelSerializer):
    question = QuestionSerializers()

    class Meta:
        model = СhoiceQuestion
        fields = ('question', )


class TestListSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    choicetest = СhoiceQuestionSerializers(many=True)

    class Meta:
        model = Test
        fields = '__all__'


class TestUpdateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Test
        fields = '__all__'


class TestDeleteSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Test
        fields = '__all__'


class QuestionCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionListSerializers(serializers.ModelSerializer):
    flags = FlagSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDeleteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDetailIDSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

