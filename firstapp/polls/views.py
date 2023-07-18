from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from datetime import datetime


def say_hello(request):
    return HttpResponse('Hello poll')


def template_poll(request):
    return render(request, 'poll_info.html')


current_datetime = datetime.now()


def list_poll(request):
    question = Question.objects.filter(start_date__lte=current_datetime, end_date__gte=current_datetime)
    # print(question)
    return render(request, 'poll_info.html', {'all_questions': question})


def detail_question_poll(request, question_id):
    qsn = Question.objects.get(id=question_id)
    return render(request, 'poll_detail.html', {'question_select': qsn})


