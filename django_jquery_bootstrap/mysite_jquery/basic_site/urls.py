from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_base, name='view_base'),
    url(r'^get_module_by_id', views.get_module_by_id, name='get_module_by_id'),
    url(r'^sec2$', views.view_sec2, name='view_sec2'),

]