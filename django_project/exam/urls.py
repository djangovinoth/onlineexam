from django.urls import path
from . import views

urlpatterns = [

    path('add-questions/', views.addquestions, name='add-questions'),
    path('edit-questions/<str:level>/<str:technology>/<str:qid>/', views.editquestions, name='edit-questions'),
    path('delete-questions/<str:level>/<str:technology>/<str:qid>/', views.deletequestions, name='delete-questions'),
    path('view-java-questions/<str:level>/<str:technology>/', views.view_java_questions, name='view-java-questions'),
    path('show_levels/<str:technology>/', views.show_levels, name='show_levels'),
    path('student_show_levels/<str:technology>/', views.student_show_levels, name='student_show_levels'),
    path('student_view_java_questions/<str:level>/<str:technology>/<str:qid>', views.student_view_java_questions, name='student_view_java_questions'),
    


]
