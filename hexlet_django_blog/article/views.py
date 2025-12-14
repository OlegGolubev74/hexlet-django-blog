from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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





# Старая версия функции (можно удалить или закомментировать):
'''
def index(request):
    return render(
        request,
        'article/index.html')
'''