from django.urls import path
from .views import *

urlpatterns = [
    path(r'test-create/', TestCreateView.as_view()),
    path(r'test-list/<int:pk>/', TestListView.as_view()),
    path(r'test-update/<int:pk>/', TestUpdateView.as_view()),
    path(r'test-delete/<int:pk>/', TestDeleteView.as_view()),
    path(r'test-detailid/<int:pk>/', TestDetailID.as_view()),

    path(r'question-create/', QuestionCreateView.as_view()),
    path(r'question-list/<int:pk>/', QuestionListView.as_view()),
    path(r'question-delete/<int:pk>/', QuestionDeleteView.as_view()),
    path(r'question-update/<int:pk>/', QuestionUpdateView.as_view()),
    path(r'question-detailid/<int:pk>/', QuestionDetailIDVIew.as_view()),
]