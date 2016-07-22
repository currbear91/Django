from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^reviews$', views.bookReview, name = 'my_book_review'),
    url(r'^specific$', views.specificReview, name = 'my_specific_review'),

]