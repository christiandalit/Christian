from django.urls import path
from . import views
from .views import deleteStudent,updateStudent
urlpatterns =[
    path('', views.index, name="homepage"),
    path('about/', views.about_page, name="aboutpage"),
    path('Student/', views.AddStudent, name="EnterNew"),
    path('Manage/', views.ManageStudent, name="Update"),
    path('delete_student/<int:pk>/', views.deleteStudent, name='delete_student'),
    path('update_student/<int:pk>/', views.updateStudent, name="update_student"),




]