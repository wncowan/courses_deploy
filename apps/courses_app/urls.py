from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^/new$', views.new),
    url(r'^/create$', views.create),
    # url(r'^/(?P<id>\d+)$', views.show),
    # url(r'^/(?P<id>\d+)/edit$', views.edit),
    url(r'^/update/(?P<id>\d+)$', views.update),
    url(r'^/destroy/(?P<id>\d+)$', views.delete),
    url(r'^/clear$', views.clear),
    url(r'^/edit/(?P<id>\d+)$', views.edit),
    url(r'^/join/(?P<id>\d+)$', views.join),
    url(r'^/show/(?P<id>\d+)$', views.show),
    # url(r'^courses/destroy/(?P<id>\d+)/confirm_delete$', views.confirm_delete),

]