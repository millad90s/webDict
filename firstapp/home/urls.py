from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('info/', views.browser_info),
]

