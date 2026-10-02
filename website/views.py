from django.shortcuts import render, redirect
from notices.models import Notice

from .models import HomeHero, SchoolStatistic, AboutSection

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import WebsiteSettings, NavigationMenu
from .forms import WebsiteSettingsForm, NavigationMenuForm

def home(request):

    heroes = (
        HomeHero.objects
        .filter(is_active=True)
        .order_by("order", "id")
    )

    about = (
        AboutSection.objects
        .filter(is_active=True)
        .first()
    )
    statistics = (
        SchoolStatistic.objects
        .filter(is_active=True)
        .order_by("order", "id")
        )

    latest_notices = (
        Notice.objects
        .order_by("-publish_date", "-created_at")[:6]
    )

    return render(
        request,
        "frontend/home.html",
        {
            "heroes": heroes,
            "about": about,
            "statistics": statistics,
            "latest_notices": latest_notices,
        }
    )

# ---------------------------------------------------------

def website_management(request):
    return render(
        request,
        "frontend/website_management.html"
    )

# ---------------------------------------------------------

class WebsiteManagementView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "website_management.html"


class WebsiteSettingsView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "website_settings.html"

    def get(self, request, *args, **kwargs):
        settings = WebsiteSettings.objects.first()
        form = WebsiteSettingsForm(instance=settings)

        return self.render_to_response({
            "form": form,
            "settings": settings,
        })

    def post(self, request, *args, **kwargs):
        settings = WebsiteSettings.objects.first()

        form = WebsiteSettingsForm(
            request.POST,
            request.FILES,
            instance=settings,
        )

        if form.is_valid():
            form.save()
            return redirect("website_settings")

        return self.render_to_response({
            "form": form,
            "settings": settings,
        })


class NavigationListView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "navigation_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["menus"] = (
            NavigationMenu.objects
            .filter(parent__isnull=True)
            .prefetch_related("children")
            .order_by("order", "name")
        )

        return context


class NavigationCreateView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "navigation_form.html"

    def get(self, request, *args, **kwargs):
        form = NavigationMenuForm()

        return self.render_to_response({
            "form": form,
            "title": "Add Navigation Menu",
        })

    def post(self, request, *args, **kwargs):
        form = NavigationMenuForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("navigation_list")

        return self.render_to_response({
            "form": form,
            "title": "Add Navigation Menu",
        })