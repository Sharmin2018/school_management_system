from django.urls import path
from .views import home, website_management


urlpatterns = [
    path("", home, name="home"),
     path(
        "website-management/",
        website_management,
        name="website_management",
    ),
]