from django.urls import path
from .views import home, website_management


from . import views

urlpatterns = [
    path("", home, name="home"),
     path(
        "website-management/",
        website_management,
        name="website_management",
    ),

    # Website Management
    path(
        "dashboard/website-management/",
        views.WebsiteManagementView.as_view(),
        name="website_management",
    ),

    path(
        "dashboard/website-management/settings/",
        views.WebsiteSettingsView.as_view(),
        name="website_settings",
    ),

    path(
        "dashboard/website-management/navigation/",
        views.NavigationListView.as_view(),
        name="navigation_list",
    ),

    path(
        "dashboard/website-management/navigation/add/",
        views.NavigationCreateView.as_view(),
        name="navigation_add",
    ),

]