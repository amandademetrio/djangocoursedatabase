from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^delete/(?P<number>[0-9]+)$', views.delete),
    url(r'^createcourse$', views.addcourse),
    url(r'^processdelete/(?P<number>[0-9]+)$', views.processdelete)
] 