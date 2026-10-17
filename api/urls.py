
from django.urls import path
from .views import hello_api, student_list_api

urlpatterns = [
    path("hello/", hello_api, name="hello_api"),
    path("students/", student_list_api, name="student_list_api"),
]
