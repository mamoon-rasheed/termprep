from django.urls import path
from . import views

urlpatterns = [
    path('retrievestudents', views.retrieve_students, name='retrieve'),
    path('studentdetails/<int:id>', views.student_details, name='details'),
    path('createstudent', views.create_student, name='create'),
    path('updatestudent/<int:id>', views.update_student, name='update'),
    path('deletestudent/<int:id>', views.delete_student, name='delete'),
]
