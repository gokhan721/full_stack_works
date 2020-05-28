from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('first_app/', views.index, name='index'),
]
