from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255, default='Untitled')
    question = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Option(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField()
