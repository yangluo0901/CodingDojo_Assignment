from django.conf.urls import url
from .  import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'signin$',views.signin_page),
    url(r'register$',views.register_page),
    url(r'signin/process$', views.signin),
    url(r'register/process$', views.register),
    url(r'dashboard/admin$',views.dashboard_admin),
    url(r'user/show/(?P<id>\d+)$',views.show, name = "show"),
    url(r'user/post$', views.post),
    url(r'user/message$',views.message),
    url(r'dashboard$', views.dashboard),
    url(r'user/edit/(?P<id>\d+)$',views.edit_page,name = "edit"),
    url(r'user/edit/process$', views.edit),
    url(r'user/edit$',views.edit_self_page),
    url(r'user/destroy/(?P<id>\d+)$', views.remove)

]
