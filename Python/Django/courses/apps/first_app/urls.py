from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'courses/add$', views.add),
    url(r'courses/destroy/(?P<id>\d+)$', views.destroy_page),
    url(r'courses/destroy/(?P<id>\d+)/confirm$', views.destroy)
]
