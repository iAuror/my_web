from django.contrib import admin

from mainapp.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
