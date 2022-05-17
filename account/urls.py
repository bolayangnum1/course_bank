from django.urls import path

from .views import RegisterListView, RegisterCreateView, RegisterDeleteView, RegisterUpdateView, RegisterDetailID, CertificateListCreateView, CertificateUpdateDestroyView, CertificateDetailID, \
    PasportUpdateDeleteView, PasportListCreateView, PasportDetailID, PhotoCreateView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView, PhotoListView

urlpatterns = [
    path(r'data-create/', RegisterCreateView.as_view()),
    path(r'data-list/', RegisterListView.as_view()),
    path(r'data-update/<int:pk>/', RegisterUpdateView.as_view()),
    path(r'data-delete/<int:pk>/', RegisterDeleteView.as_view()),
    path(r'data-detailID/<int:pk>/', RegisterDetailID.as_view()),

    path(r'photo-detail/<int:pk>/', PhotoDetailView.as_view()),
    path(r'photo-create/', PhotoCreateView.as_view()),
    path(r'photo-update/<int:pk>/', PhotoUpdateView.as_view()),
    path(r'photo-list/', PhotoListView.as_view()),
    path(r'photo-delete/<int:pk>/', PhotoDeleteView.as_view()),

    path(r'pasport-createlist/<int:pk>/', PasportListCreateView.as_view()),
    path(r'pasport-updatedelete/<int:pk>/', PasportUpdateDeleteView.as_view()),
    path(r'pasport-detail/<int:pk>/,', PasportDetailID.as_view()),

    path(r'certificate-createlist/<int:pk>/', CertificateListCreateView.as_view()),
    path(r'certificate-updatedelete/<int:pk>/', CertificateUpdateDestroyView.as_view()),
    path(r'certificate-detailID/<int:pk>', CertificateDetailID.as_view()),

]
