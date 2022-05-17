from django.contrib import admin
from .models import СhoiceQuestion, Flag, Question, Test


class Flag_inlini(admin.StackedInline):
    model = Flag
    extra = 0


class СhoiceQuetion_inlini(admin.StackedInline):
    model = СhoiceQuestion
    extra = 0


class FlagAdmin(admin.ModelAdmin):
    inlines = [Flag_inlini]
    list_display = ('title', )
    list_filter = ('title', )
    search_fields = ('title', )


class ChoiceQuetionAdmin(admin.ModelAdmin):
    inlines = [СhoiceQuetion_inlini]
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Question, FlagAdmin)
admin.site.register(Test, ChoiceQuetionAdmin)

