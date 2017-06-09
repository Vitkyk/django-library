from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^author/$', views.authors, name='authors'),
    url(r'^books/(?P<id>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^books/new/$', views.book_new, name='book_new'),
    url(r'^books/$', views.books, name='books'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]