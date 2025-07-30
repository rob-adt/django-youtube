from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("download_video/<int:video_pk>", views.download_video),
    path("download_audio/<int:video_pk>", views.download_audio),
    path("", views.detailView.as_view(), name="detail")
]