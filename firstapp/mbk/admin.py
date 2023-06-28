from django.contrib import admin

# Register your models here.
from .models import Theory, SupportiveFact

admin.site.register(Theory)
admin.site.register(SupportiveFact)