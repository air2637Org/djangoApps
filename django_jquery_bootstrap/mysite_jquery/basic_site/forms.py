from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import Module, Teacher

class ModuleModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

class AssignTeacherToModuleForm(forms.Form):
    module_name = ModuleModelChoiceField(queryset=Module.objects.all())
    num_of_students = forms.IntegerField()
    teacher_name = forms.ModelChoiceField(queryset=Teacher.objects.all())

