from django.urls import path

from hexlet_django_blog.tovary import views

urlpatterns = [
    path("", views.index),
]
