from django.shortcuts import render, get_object_or_404 #<--get_object_or_404 добавили в уроке 15 Просмотр (CRUD) 
from django.http import HttpResponse
from django.views import View


from hexlet_django_blog.article.models import Article


#урок 14 Список (CRUD)
class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15] # <-Первой строкой из базы извлекаются 15 первых статей
        return render(
            request,
            "article/index.html",
            context={
                "articles": articles,
            },
        )
    

#добавили в уроке 15 Просмотр (CRUD) 
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "article/show.html",
            context={
                "article": article,
            },
        )







#сама первая версия вьюхи
'''
class IndexView(View):
    """
    Класс-представление для главной страницы статей.
    Наследует базовый класс View.
    """
    
    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запросы.
        Аналог функции index(request), но для класса.
        """
        return render(
            request,
            'article/index.html'
        )
    
    # Можно добавить обработку других методов HTTP:
    # def post(self, request, *args, **kwargs):
    #     return HttpResponse("POST запрос на страницу статей")
    
    # def put(self, request, *args, **kwargs):
    #     return HttpResponse("PUT запрос")
    
    # def delete(self, request, *args, **kwargs):
    #     return HttpResponse("DELETE запрос")
'''


'''
http://localhost:8000/articles/e/4/ для такого запроса
class IndexView(View):
    """
    Класс-представление для отображения статьи по тегу и ID.
    """
    
    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запросы.
        Получает параметры из URL: tags и article_id.
        """
        # Извлекаем параметры из kwargs
        tags = kwargs.get('tags', '')
        article_id = kwargs.get('article_id', 0)
        
        # Формируем и возвращаем ответ
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")

'''



# Старая версия функции (можно удалить или закомментировать):
#версия без классов
'''
def index(request):
    return render(
        request,
        'article/index.html')
'''