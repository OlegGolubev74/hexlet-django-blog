from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

'''
def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "World! Это самая главная страница сайта!",
        },
    )
'''


#до рекализации редирект с главной страницы сайта на http://localhost:8000/articles/python/42/ 
#главная страница открывается ок
'''
class IndexView(TemplateView):
    """
    Класс-представление для главной страницы.
    Наследует TemplateView и переопределяет контекст.
    """
    #Указываем, какой шаблон использовать
    #Эквивалентно template_name="index.html" в render()
    template_name = "index.html"
    
    #Переопределение контекста
    def get_context_data(self, **kwargs): #метод, который собирает контекст для шаблона
        """
        Переопределяем метод для добавления своего контекста.
        """
        # Получаем контекст родительского класса
        context = super().get_context_data(**kwargs)
        
        # Добавляем свои данные в контекст
        context["who"] = "World! Это самая главная страница сайта!"
        
        return context

'''


#реализован редирект с главной страницы сайта на http://localhost:8000/articles/python/42/ 
class IndexView(TemplateView):
    """
    Класс-представление для главной страницы.
    Теперь перенаправляет на статью python/42.
    """
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запросы.
        Вместо рендеринга шаблона делает перенаправление.
        """
        # Используем reverse для получения URL по имени маршрута
        # Имя 'article' должно быть задано в urls.py приложения article
        redirect_url = reverse(
            'article',  # имя маршрута
            kwargs={    # параметры для подстановки в URL
                'tags': 'python',
                'article_id': 42
            }
        )
        
        # Альтернативный вариант с args вместо kwargs:
        # redirect_url = reverse('article', args=['python', 42])
        
        # Перенаправляем пользователя
        return redirect(redirect_url)
    
    # Метод get_context_data больше не нужен, так как мы не рендерим шаблон
    # но можно оставить, если в будущем снова понадобится рендерить шаблон






'''
def about(request):
    return render(request, "about.html")
'''

def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )