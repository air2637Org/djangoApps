# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "name : {0}".format(self.name)


class Module(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    num_of_student = models.IntegerField(default=0)
    teacher = models.ForeignKey(Teacher, null=True, related_name='modules')

    def __str__(self):
        return "name : {0}, num_of_student: {1}".format(self.name, self.num_of_student)