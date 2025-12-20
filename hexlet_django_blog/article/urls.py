from django.urls import path

from hexlet_django_blog.article import views
#from hexlet_django_blog.article.views import IndexView
from hexlet_django_blog.article.views import IndexView, ArticleView #добавили в уроке 15 Просмотр (CRUD) 

#добавили в уроке 15 Просмотр (CRUD)
 
#urlpatterns = [
 #   path("", IndexView.as_view()),
  #  path("<int:id>/", ArticleView.as_view()),#/articles/1/ например
#]

urlpatterns = [
    path("", IndexView.as_view(), name="article_list"),
    path("<int:id>/", ArticleView.as_view(), name="article_detail"),  # добавляем name
]

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

#urlpatterns = [
 #   path("", IndexView.as_view()),
#]

'''
urlpatterns = [
    # Обрабатываем путь с параметрами: /articles/tags/article_id/
    path("<str:tags>/<int:article_id>/", views.IndexView.as_view(), name="article"), # http://localhost:8000/articles/e/4/
    
    # Можно оставить и корневой путь для списка статей (если нужно):
    #path("", views.IndexView.as_view(), name="article_list"),
]

'''