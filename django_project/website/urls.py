from django.urls import path
from . import views

urlpatterns = [

    path('websitehome/', views.websitehome, name='websitehome'),


]
