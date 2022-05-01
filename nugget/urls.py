from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('post/<str:pk>',views.post,name='post'),
    path('list',views.list,name='list'),
    path('about',views.about,name='about')
]