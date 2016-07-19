from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),  #Make a form for adding an email  
    url(r'^', views.create_email), #receive that form

]