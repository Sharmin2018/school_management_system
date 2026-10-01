from django.shortcuts import render
from notices.models import Notice

from .models import HomeHero, SchoolStatistic, AboutSection


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
    