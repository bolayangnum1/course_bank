from django.urls import path
from topik.views import *


urlpatterns = [
    path(r'topik-create/', TopikCreateView.as_view()),
    path(r'topik-list/', TopikListView.as_view()),
    path(r'topik-update/<int:pk>/', TopikUpdateView.as_view()),
    path(r'topik-delete/<int:pk>/', TopikDeleteView.as_view()),
    path(r'topik-detail/<int:pk>', TopikDetail.as_view()),

    path(r'topicmain-detail/<int:pk>/', TopicMainDetailView.as_view()),
    path(r'topicmain-list/<int:pk>/', TopicMainListView.as_view()),
    path(r'topicmain-create/', TopicMainCreateView.as_view()),
    path(r'topicmain-delete/<int:pk>/', TopicMainDeleteView.as_view()),
    path(r'topicmain-update/<int:pk>/', TopicMainUpdateView.as_view()),
]