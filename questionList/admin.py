from django.contrib import admin
from .models import QuestionList, QueDoneByUser

# Register your models here.

admin.site.register(QuestionList)
admin.site.register(QueDoneByUser)
