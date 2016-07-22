from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_dissapear_index'),
    url(r'^ninjas$', views.showNinjas, name = 'my_ninja'),
 	url(r'^ninjas/(?P<color>\w+)$', views.show, name = 'my_ninjacolor')

]