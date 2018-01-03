from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^main$', views.index),
    url(r'^registration$', views.register),
    url(r'^login$', views.login),
    url(r'^quotes$', views.all_quotes),
    url(r'^add_quote$',views.add_quote),
    url(r'^add_favorite$', views.add_favorite),
    url(r'^remove_favorite$',views.remove_favorite),
    url(r'^users/(?P<id>\d+)$', views.individual),
]
