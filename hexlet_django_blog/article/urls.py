from django.urls import path

from hexlet_django_blog.article import views

'''
urlpatterns = [
    path("", views.index),
]
'''

urlpatterns = [
    # Используем класс IndexView с вызовом as_view()
    path("", views.IndexView.as_view()),
]