from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'home$', views.home_page),
    url(r'register$', views.register),
    url(r'signin$', views.signin),
    url(r'books$',views.books),
    url(r'books/add$', views.add_page),
    url(r'books/add/process$',views.add_books),
    url(r'books/(?P<id>\d+)$',views.book_page, name = "book_page"),
    url(r'reviews/add', views.add_review),
    url(r'reviews/delete/(?P<id>\d+)/(?P<book_id>\d+)$',views.delete, name = "delete"),
    url(r'users/(?P<id>\d+)$', views.user)
]
