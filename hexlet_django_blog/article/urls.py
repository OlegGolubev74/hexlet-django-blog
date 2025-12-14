from django.urls import path

from hexlet_django_blog.article import views

'''
urlpatterns = [
    path("", views.index),
]
'''


'''
urlpatterns = [
    # Используем класс IndexView с вызовом as_view()
    path("", views.IndexView.as_view()),
]
'''

urlpatterns = [
    # Обрабатываем путь с параметрами: /articles/tags/article_id/
    path("<str:tags>/<int:article_id>/", views.IndexView.as_view(), name="article"),
    
    # Можно оставить и корневой путь для списка статей (если нужно):
    # path("", views.IndexView.as_view(), name="article_list"),
]