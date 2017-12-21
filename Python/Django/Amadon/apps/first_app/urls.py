from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'amadon$', views.purchase),
    url(r'amadon/purchase$',views.process),
    url(r'amadon/checkout$',views.checkout),
    url(r'amadon/clear$',views.clear)
]
