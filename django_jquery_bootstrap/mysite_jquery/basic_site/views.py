# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Teacher, Module
from .forms import AssignTeacherToModuleForm

from django.core import serializers
from django.http import HttpResponse

# Create your views here.


def view_base(request):
    form = AssignTeacherToModuleForm()
    return render(request, 'sec1.html', {'form': form})

def get_module_by_id(request):
    search_id = None
    if request.method == 'GET':
        search_id = request.GET['id']
        searched_module = Module.objects.get(id=search_id)
    serialized_obj = None
    if searched_module:
        serialized_obj = serializers.serialize('json', [ searched_module, ])
    bytes = serialized_obj.encode('utf-8')
    return HttpResponse(bytes, content_type='application/json') 

def view_sec2(request):
    return render(request, 'sec2.html')
