from django.urls import path
from . import views

urlpatterns = [

    path('', views.websitehome, name='websitehome'),
    path('selenium', views.selenium, name='selenium'),

]
