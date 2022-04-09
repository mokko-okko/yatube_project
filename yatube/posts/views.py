from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
        'если у тебя нет правильных <s>вопросов</s> запросов.'
    ) 

def group_posts(request):
    return HttpResponse(
        'Ты <i> можешь</i> получить правильные <b>ответы</b>,<br> '
        'если нет правильных <s>вопросов</s> запросов.'
    ) 