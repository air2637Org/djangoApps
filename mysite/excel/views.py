# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django import forms
import django_excel as excel
from excel.models import Question, Choice
import pandas


class UploadFileForm(forms.Form):
    file = forms.FileField()

# Create your views here.
def import_data(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)

            def choice_func(row):
                # import pdb; pdb.set_trace()
                question_obj = Question.objects.filter(slug=row[0])[0]
                row[0] = question_obj
                return row

            if form.is_valid():
                filehandle = request.FILES['file']
                import pdb; pdb.set_trace()

                xl = pandas.ExcelFile(filehandle)
                df_question = xl.parse('question')
                question_arr = df_question.to_dict('records')
                question_models = []
                for item in question_arr:
                    question_model_obj = Question(question_text = item['Question Text'],
                            pub_date = item['Publish Date'],
                            slug = item['Unique Identifier'])
                    question_models.append(question_model_obj)
                
                import pdb; pdb.set_trace()
                Question.objects.bulk_create(question_models)
                

                # filehandle.save_book_to_database(
                #     models=[Question, Choice],
                #     initializers = [None, choice_func],
                #     mapdicts = [
                #         {
                #         "Question Text": "question_text",
                #         "Publish Date": "pub_date",
                #         "test": None,
                #         "Unique Identifier": "slug",
                #         "test2": None
                #         },
                #         # ['question_text', 'pub_date', 'slug'],
                #         ['question', 'choice_text', 'votes']
                #     ]
                # )
                # return redirect('handson_view')
            else:
                return HttpResponseBadRequest()
        else:
            form = UploadFileForm()
        return render(request, 'upload_form.html', {
                    'form': form,
                    'title': 'Import Excel data into DB',
                    'header': 'Upload sample-data.xls to save it into DB:'
                })