# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Teacher, Module

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_of_student', 'teacher',)    

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Module, ModuleAdmin)
