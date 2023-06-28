from django.db import models


# Create your models here.
class Theory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SupportiveFact(models.Model):
    theory = models.ForeignKey(Theory, on_delete=models.CASCADE)
    description = models.TextField()
