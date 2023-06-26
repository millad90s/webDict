from django.shortcuts import render
from .models import Theory
from django.db import models


# Create your views here.


def list_theory(request):
    theories = Theory.objects.all()
    print(theories)
    return render(request, 'theory_list.html', {'all_theory': theories})

