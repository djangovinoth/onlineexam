from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('exam-java/', views.javaexam, name='exam-java'),
    path('java-level/', views.javalevel, name='java-level'),


]
