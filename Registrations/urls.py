from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("accounts.urls",namespace="accounts")),
    path("home/",include("student.urls",namespace="student")),

]
