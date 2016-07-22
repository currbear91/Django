from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_course_index'),
    url(r'^process$', views.process, name = 'my_course_process'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'my_course_delete'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'my_course_destroy'),
    url(r'^usercourse$', views.usercourse, name = 'my_usercourse'),

]
