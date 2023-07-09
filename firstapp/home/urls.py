from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('info/', views.show_info),
]

