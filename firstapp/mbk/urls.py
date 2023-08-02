from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_theory),
    path('mbkdetail/<int:theory_id>', views.detail_theory_mbk),
]

