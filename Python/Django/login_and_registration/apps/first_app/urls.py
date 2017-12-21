from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'login$', views.login),
    url(r'registration$', views.registration),
    url(r'success$', views.success)
]
