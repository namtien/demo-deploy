from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^deploy$', views.index, name='index')
]
