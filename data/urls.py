from django.urls import path
from .views import *


urlpatterns = [
    path(r'contact-create/', ContactCreateView.as_view()),
    path(r'contact-list/', ContactListView.as_view()),
    path(r'contact-update/<int:pk>/', ContactUpdateView.as_view()),
    path(r'contact-delete/<int:pk>/', ContactDeleteView.as_view()),

    path(r'props-create/', BankCreateView.as_view()),
    path(r'props-list/', BankListView.as_view()),
    path(r'props-update/<int:pk>/', BankUpdateView.as_view()),
    path(r'props-delete/<int:pk>/', BankDeleteView.as_view()),

    path(r'about-createlist/', AboutListCreateView.as_view()),
    path(r'about-updatedelete/', AboutUpdateDeleteView.as_view()),
]