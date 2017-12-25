# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug',
                    'author', 'publish', 'status')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
