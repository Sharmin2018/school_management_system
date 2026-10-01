from django.urls import path

from .views import (
    DashboardView,
    WebsiteManagementView,
)

urlpatterns = [

    path(
        "dashboard/",
        DashboardView.as_view(),
        name="dashboard",
    ),

    path(
        "website-management/",
        WebsiteManagementView.as_view(),
        name="website_management",
    ),
]