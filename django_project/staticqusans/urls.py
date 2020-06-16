from django.urls import path
from . import views


urlpatterns = [

     path('staticqusans/', views.staticqusans, name='staticqusans'),
     path('showques/<str:technology>/', views.showques, name='showques'),
     path('showques_std/<str:technology>/', views.showques_std, name='showques_std'),
     path('addques/', views.addques, name='addques'),
     path('deletequestions/<str:technology>/<str:id>', views.deletequestions, name='deletequestions'),

     path('editquestions/<str:technology>/<str:id>', views.editquestions, name='editquestions'),


]
