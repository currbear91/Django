from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.indexs, name = "my_semi_indexs"),
    url(r'^shows/(?P<id>\d+)$', views.shows, name = "my_semi_shows"),
    url(r'^edits/(?P<id>\d+)$', views.edits, name = "my_semi_edits"),   
    url(r'^news$', views.news, name = "my_semi_news"),
    url(r'^updates/(?P<id>\d+)$', views.updates, name = "my_semi_updates"),
    url(r'^creates$', views.creates, name = "my_semi_creates"),
   	url(r'^destroys/(?P<id>\d+)$', views.destroys, name = "my_semi_destroys"),


]
