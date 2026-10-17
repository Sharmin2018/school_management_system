from django.urls import path
from . import views
from .views import (
    HomeHeroListView,
    HomeHeroCreateView,
    HomeHeroUpdateView,
    HomeHeroDeleteView,
)

urlpatterns = [

    # Public Website
    path(
        "",
        views.home,
        name="home",
    ),
    path(
    "<slug:slug>/",
    views.WebsitePageDetailView.as_view(),
    name="website_page_detail",
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

    path(
    "dashboard/website-management/pages/",
    views.WebsitePageListView.as_view(),
    name="website_page_list",
    ),

    path(
    "dashboard/website-management/pages/add/",
    views.WebsitePageCreateView.as_view(),
    name="website_page_add",
    ),

    path(
    "dashboard/website-management/pages/edit/<int:id>/",
    views.WebsitePageUpdateView.as_view(),
    name="website_page_edit",
    ),

    path(
    "dashboard/website-management/pages/delete/<int:id>/",
    views.WebsitePageDeleteView.as_view(),
    name="website_page_delete",
    ),

    path(
    "dashboard/website-management/hero/",
    HomeHeroListView.as_view(),
    name="hero_list",
    ),
    path(
    "dashboard/website-management/hero/add/",
    HomeHeroCreateView.as_view(),
    name="hero_add",
    ),
    path(
    "dashboard/website-management/hero/edit/<int:id>/",
    HomeHeroUpdateView.as_view(),
    name="hero_edit",
    ),
    path(
    "dashboard/website-management/hero/delete/<int:id>/",
    HomeHeroDeleteView.as_view(),
    name="hero_delete",
    ),
    path(
    "dashboard/website-management/about/",
    views.AboutSectionView.as_view(),
    name="about_management",
    ),
    
path(
    "dashboard/website-management/statistics/",
    views.SchoolStatisticListView.as_view(),
    name="statistic_list",
),
path(
    "dashboard/website-management/statistics/add/",
    views.SchoolStatisticCreateView.as_view(),
    name="statistic_add",
),
path(
    "dashboard/website-management/statistics/edit/<int:id>/",
    views.SchoolStatisticUpdateView.as_view(),
    name="statistic_edit",
),
path(
    "dashboard/website-management/statistics/delete/<int:id>/",
    views.SchoolStatisticDeleteView.as_view(),
    name="statistic_delete",
),


path(
    "dashboard/website-management/facilities/",
    views.SchoolFacilityListView.as_view(),
    name="facility_list",
),
path(
    "dashboard/website-management/facilities/add/",
    views.SchoolFacilityCreateView.as_view(),
    name="facility_add",
),
path(
    "dashboard/website-management/facilities/edit/<int:id>/",
    views.SchoolFacilityUpdateView.as_view(),
    name="facility_edit",
),
path(
    "dashboard/website-management/facilities/delete/<int:id>/",
    views.SchoolFacilityDeleteView.as_view(),
    name="facility_delete",
),

path(
    "dashboard/website-management/principal-message/",
    views.PrincipalMessageListView.as_view(),
    name="principal_message_list",
),
path(
    "dashboard/website-management/principal-message/add/",
    views.PrincipalMessageCreateView.as_view(),
    name="principal_message_add",
),
path(
    "dashboard/website-management/principal-message/edit/<int:id>/",
    views.PrincipalMessageUpdateView.as_view(),
    name="principal_message_edit",
),
path(
    "dashboard/website-management/principal-message/delete/<int:id>/",
    views.PrincipalMessageDeleteView.as_view(),
    name="principal_message_delete",
),

]