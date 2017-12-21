from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'session_word/$', views.index),
    url(r'session_word/process$', views.process),
    url(r'session_word/clear$', views.clear)
]
