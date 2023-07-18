from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_poll),
    path('polldetail/<int:question_id>', views.detail_question_poll),
               ]