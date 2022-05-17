from django.contrib import admin
from .models import *


class Fileinlini(admin.StackedInline):
    model = File
    extra = 0


class Videoinlini(admin.StackedInline):
    model = Video
    extra = 0


class ChoiceTopic(admin.StackedInline):
    model = ChoiceTopic
    extra = 0


class Topicadmin(admin.ModelAdmin):
    inlines = [Fileinlini, Videoinlini]
    list_display = ('user', 'name_work')
    list_filter = ('user', 'name_work')
    search_fields = ('user', 'name_work')


class ChoiceTopicadmin(admin.ModelAdmin):
    inlines = [ChoiceTopic]
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(TopicMain, ChoiceTopicadmin)
admin.site.register(Topic, Topicadmin)


