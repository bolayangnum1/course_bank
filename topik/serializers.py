from rest_framework import serializers
from .models import *


class VideoSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Video
        fields = '__all__'


class FileSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = File
        fields = '__all__'


class TopikCreateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Topic
        fields = '__all__'


class TopikListSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Topic
        fields = '__all__'


class TopikUpdateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Topic
        fields = '__all__'


class TopikDeleteSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Topic
        fields = '__all__'


class TopikDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    files = FileSerializers(many=True)
    videos = VideoSerializers(many=True)

    class Meta:
        model = Topic
        fields = '__all__'


class TopicMainDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TopicMain
        fields = '__all__'


class ChoiceTopicSerializer(serializers.ModelSerializer):
    topicmain = TopicMainDetailSerializer()
    topics = TopikDetailSerializers()

    class Meta:
        model = ChoiceTopic
        fields = '__all__'

