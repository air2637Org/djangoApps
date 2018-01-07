# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class QuestionAdmin (admin.ModelAdmin):
    list_display = ('question_text', 'pub_date','slug')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)