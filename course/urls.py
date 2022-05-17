from django.urls import path
from course.views import CourseDetail, CoursesDeleteView, CoursesUpdateView, CoursesCreateView, \
                         CoursesListView, ScoreboardCreateListView, ScoreboardDetailView, ScoreboardDeleteUpdateView,\
                         SubscriptionCreate, SubscriptionDetail, SubscriptionUpdate, SubscriptionDelete, SubscriptionList,\
                         ApplicationToAdminCreate, ApplicationToAdminList, ApplicationToAdminUpdate, ApplicationToAdminDetail, ApplicationToAdminDelete

from . import views

urlpatterns = [
    path(r'index/<int:course_id>/', views.IndexAPIview.as_view()),

    path(r'course-create/', CoursesCreateView.as_view()),
    path(r'course-list/', CoursesListView.as_view()),
    path(r'course-update/<int:pk>/', CoursesUpdateView.as_view()),
    path(r'course-delete/<int:pk>/', CoursesDeleteView.as_view()),
    path(r'course-detail/<int:pk>/', CourseDetail.as_view()),

    path(r'scoreboard-Create-list/', ScoreboardCreateListView.as_view()),
    path(r'scoreboard-UpdateDelete/<int:pk>/', ScoreboardDeleteUpdateView.as_view()),
    path(r'scoreboard-Detail/<int:pk>/', ScoreboardDetailView.as_view()),

    path(r'ApplicationToAdmin-Create/', ApplicationToAdminCreate.as_view()),
    path(r'ApplicationToAdmin-List/', ApplicationToAdminList.as_view()),
    path(r'ApplicationToAdmin-Detail/<int:pk>/', ApplicationToAdminDetail.as_view()),
    path(r'ApplicationToAdmin-Delete/<int:pk>/', ApplicationToAdminDelete.as_view()),
    path(r'ApplicationToAdmin-Update/<int:pk>/', ApplicationToAdminUpdate.as_view()),

    path(r'Subscription-create/', SubscriptionCreate.as_view()),
    path(r'Subscription-list/', SubscriptionList.as_view()),
    path(r'Subscription-update/int:pk/', SubscriptionUpdate.as_view()),
    path(r'Subscription-delete/int:pk/', SubscriptionDelete.as_view()),
    path(r'Subscription-detail/int:pk/', SubscriptionDetail.as_view()),
]