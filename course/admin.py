from django.contrib import admin
from .models import TextCourse, Course, ChoiceTopicCourse, Scoreboard, Subscription, ApplicationToAdmin


class Textinlini(admin.StackedInline):
    model = TextCourse
    extra = 0


class ChoiceTopicinlini(admin.StackedInline):
    model = ChoiceTopicCourse
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [ChoiceTopicinlini, Textinlini]
    list_display = ['title', 'types', 'price', 'time_work']
    list_filter = ['title', 'types', 'price', 'time_work']
    search_fields = ['title']
    date_hierarchy = 'created_date'
    ordering = ('title',)


class ScoreboardAdmin(admin.ModelAdmin):
    list_display = ['course', 'score', 'user', 'quiz_room']
    list_filter = ['course', 'score', 'user', 'quiz_room']
    search_fields = ['course', 'score', 'user', 'quiz_room']


class ApplicationToAdminAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'activation']
    list_filter = ['id', 'user', 'activation']
    search_fields = ['id', 'user', 'activation']
    ordering = ('created_date',)
    date_hierarchy = 'created_date'


class SubscriptionadAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'subscription']
    list_filter = ['id', 'user', 'subscription']
    search_fields = ['id', 'user', 'subscription']


admin.site.register(Course, CourseAdmin)
admin.site.register(Scoreboard, ScoreboardAdmin)
admin.site.register(Subscription, SubscriptionadAdmin)
admin.site.register(ApplicationToAdmin, ApplicationToAdminAdmin)
