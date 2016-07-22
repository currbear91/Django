from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_word_index'),
    url(r'^process$', views.formProcess, name = 'my_word_process'),
    url(r'^reset$', views.deleteCount, name = 'my_word_reset')



]
