from django.urls import path
from . import views

urlpatterns = [

    # Public Website
    path(
        "",
        views.home,
        name="home",
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
    path(
    "dashboard/website-management/navigation/edit/<int:id>/",
    views.NavigationUpdateView.as_view(),
    name="navigation_edit",
    ),

    path(
    "dashboard/website-management/navigation/delete/<int:id>/",
    views.NavigationDeleteView.as_view(),
    name="navigation_delete",
),
]