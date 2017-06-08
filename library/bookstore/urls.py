from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^author/$', views.authors, name='index'),
    url(r'^books/(?P<id>[0-9]+)/$', views.book_detail),
    url(r'^books/$', views.books, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]