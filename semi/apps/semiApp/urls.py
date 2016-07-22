from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.indexs),
    url(r'^shows/(?P<id>\d+)$', views.shows),
    url(r'^edits/(?P<id>\d+)$', views.edits),   
    url(r'^news$', views.news),
    url(r'^updates/(?P<id>\d+)$', views.updates),
    url(r'^creates$', views.creates),
   	url(r'^destroys/(?P<id>\d+)$', views.destroys),


]
