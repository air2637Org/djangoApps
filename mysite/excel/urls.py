from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload/$', views.import_data, name='import_data'),
]