

from django.urls import path
from . import views




urlpatterns = [
    
    path('mentor/<int:mentor_id>/', views.mentor_details, name='mentor_details'),
    path('mentorship/students/<int:student_id>/', views.student_details, name='student_details'),
    path('mentor/', views.mentor, name='mentor'),
    path('student/', views.student, name='student'),
    path('students/<int:student_id>/', views.student_details, name='student_details'),
    path('', views.home, name='home'),  # Route for the home page
    path('dashboard/', views.dashboard, name='dashboard'),
     

]