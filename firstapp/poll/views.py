from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def say_hello(request):
    return HttpResponse('Hello poll')


def template_poll(request):
    return render(request, 'poll_info.html')


def list_poll(request):
    question = Question.objects.all()
    print(question)
    return render(request, 'poll_info.html', {'all_questions': question})
