from django.shortcuts import render,HttpResponse, get_object_or_404
from django.template import loader
# Create your views here.
from .models import Post, Group

def index(request):
    
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title = ''
    
    context = {
            # В словарь можно передать переменную
            'title': title,
            # А можно сразу записать значение в словарь. Но обычно так не делают
            'posts': posts,
                }
    return render(request, template, context) 

def group_posts(request, post_slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=post_slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'group_title': group.title,
        'group_description': group.description
    }
    return render(request, 'posts/group_list.html', context) 
    


