from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index, name = "my_user_index")

]
