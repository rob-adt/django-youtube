from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("download_video", views.download_video)
]