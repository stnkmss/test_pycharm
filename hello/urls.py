from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create')
    # url(r'', HelloView.as_view(), name='index')
    # path('', views.index, name='index'),
    # path('form', views.form, name='form')
    # path('next', views.next, name='next')
]