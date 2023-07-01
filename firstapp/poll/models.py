from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)


class Option(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField()



