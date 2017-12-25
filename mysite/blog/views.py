# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail, get_connection
from django.db.models import Count
from taggit.models import Tag
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    # import pdb; pdb.set_trace()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
        
    # add page
    paginator = Paginator(object_list, 3)
    currentpage = request.GET.get('page')
    try:
        posts = paginator.page(currentpage)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,\
                    'blog/post/list.html',\
                    {'posts': posts,\
                    'currentpage': currentpage,\
                    'tag': tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,slug=post,\
                                    status='published',\
                                    publish__year=year,\
                                    publish__month=month,\
                                    publish__day=day)
    comments = post.comments.filter(active = True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment_obj = comment_form.save(commit=False)
            new_comment_obj.post = post
            new_comment_obj.save()

    else:
        comment_form = CommentForm()

    # import pdb; pdb.set_trace()
    # post_tags_ids = post.tags.value_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__in = post_tags_ids).exclude(id=post.id)
    
    post_tags_names = post.tags.names()
    similar_posts = Post.published.filter(tags__name__in=post_tags_names).exclude(id=post.id)

    similar_posts = similar_posts.annotate(same_tags = Count('tags')).order_by('-same_tags', '-publish')[:4]
    
    return render(request, 'blog/post/detail.html', \
                        {'post': post,\
                        'comments': comments,\
                        'comment_form': comment_form,\
                        'similar_posts': similar_posts})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status ='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')

            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommands you reading "{}" '.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{} \'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']], connection=con )
            #reference can be found https://djangobook.com/tying-forms-views/
            sent = True
            
    # the view display an empty form if the url is in GET
    else:
        form = EmailPostForm()
        
    return render(request, 'blog/post/share.html',\
                            {'post': post,\
                            'form': form,\
                            'sent': sent})
