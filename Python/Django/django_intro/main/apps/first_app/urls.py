from django.con.urls import urls
from . import views

urlpatterns = [
    url(r'^$', views.index)
]
