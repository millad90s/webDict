from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World Django')


def browser_info(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    return render(request, 'browser_info.html', {'browser_name': user_agent})

