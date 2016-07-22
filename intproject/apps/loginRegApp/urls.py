from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_login_index'),
    url(r'^process$', views.process, name = 'my_login_process'),
    url(r'^success$', views.success, name = 'my_login_success')


]