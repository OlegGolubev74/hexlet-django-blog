from django.shortcuts import render
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