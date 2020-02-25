from django.urls import path
from . views import StudentView,student_registration,edit,delete
 
app_name="school"

urlpatterns=[
    path("",StudentView.as_view(),name="home"),
    path("registration/",student_registration,name="registration"),
    path("edit/<slug:slug>/",edit,name="edit"),
    path("delete/<slug:slug>/",delete,name="delete")
]