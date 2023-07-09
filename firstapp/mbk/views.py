from django.shortcuts import render
from .models import Theory
from django.db import models


# Create your views here.


def list_theory(request):
    theories = Theory.objects.all()
    print(theories)
    return render(request, 'theory_list.html', {'all_theory': theories})


def detail_theory_mbk(request, theory_id):
    theo = Theory.objects.get(id=theory_id)
    return render(request, 'theory_detail.html', {'theory_select': theo})
