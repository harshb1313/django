from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('students/', views.StudentsApi.as_view(), name='students_api'),
    # path('students/', views.student_list, name='student_list'),
    # path('students/add/', views.add_student, name='add_student'),
    # path('students/update/<int:id>/', views.update_student, name='update_student'),
    # path('students/partial-update/<int:id>/', views.patial_update_student, name='partial_update_student'),
    # path('students/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('books/', views.api_books, name='api_books'),
]
