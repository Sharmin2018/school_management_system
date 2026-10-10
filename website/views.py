from django.shortcuts import render, redirect
from notices.models import Notice

from .models import HomeHero, SchoolStatistic, AboutSection, WebsitePage

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import WebsiteSettings, NavigationMenu

from .forms import (
    WebsiteSettingsForm,
    NavigationMenuForm,
    WebsitePageForm,
    HomeHeroForm,
    AboutSectionForm,
)

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
    
    template_name = "website/website_management.html"


class WebsiteSettingsView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "website/website_settings.html"

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
    template_name = "website/navigation_list.html"

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
    template_name = "website/navigation_form.html"

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

class NavigationUpdateView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "website/navigation_form.html"

    def get(self, request, *args, **kwargs):
        menu = NavigationMenu.objects.get(id=kwargs["id"])
        form = NavigationMenuForm(instance=menu)

        return self.render_to_response({
            "form": form,
            "title": "Edit Navigation Menu",
            "menu": menu,
        })

    def post(self, request, *args, **kwargs):
        menu = NavigationMenu.objects.get(id=kwargs["id"])

        form = NavigationMenuForm(
            request.POST,
            instance=menu,
        )

        if form.is_valid():
            form.save()
            return redirect("navigation_list")

        return self.render_to_response({
            "form": form,
            "title": "Edit Navigation Menu",
            "menu": menu,
        })

class NavigationDeleteView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "website/navigation_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        menu = NavigationMenu.objects.get(id=kwargs["id"])

        return self.render_to_response({
            "menu": menu,
        })

    def post(self, request, *args, **kwargs):
        menu = NavigationMenu.objects.get(id=kwargs["id"])
        menu.delete()

        return redirect("navigation_list")

class WebsitePageCreateView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "website/page_form.html"

    def get(self, request, *args, **kwargs):
        form = WebsitePageForm()

        return self.render_to_response({
            "form": form,
            "title": "Add Website Page",
        })

    def post(self, request, *args, **kwargs):
        form = WebsitePageForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()
            return redirect("website_page_list")

        return self.render_to_response({
            "form": form,
            "title": "Add Website Page",
        })

class WebsitePageUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "website/page_form.html"

    def get(self, request, *args, **kwargs):
        page = WebsitePage.objects.get(id=kwargs["id"])
        form = WebsitePageForm(instance=page)

        return self.render_to_response({
            "form": form,
            "title": "Edit Website Page",
            "page": page,
        })

    def post(self, request, *args, **kwargs):
        page = WebsitePage.objects.get(id=kwargs["id"])
        form = WebsitePageForm(
            request.POST,
            request.FILES,
            instance=page
        )

        if form.is_valid():
            form.save()
            return redirect("website_page_list")

        return self.render_to_response({
            "form": form,
            "title": "Edit Website Page",
            "page": page,
        })

class WebsitePageDeleteView(LoginRequiredMixin, TemplateView):
    template_name = "website/page_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        page = WebsitePage.objects.get(id=kwargs["id"])

        return self.render_to_response({
            "page": page,
        })

    def post(self, request, *args, **kwargs):
        page = WebsitePage.objects.get(id=kwargs["id"])
        page.delete()

        return redirect("website_page_list")

class WebsitePageListView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "website/page_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["pages"] = WebsitePage.objects.all()

        return context

class WebsitePageDetailView(TemplateView):
    template_name = "frontend/page_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = kwargs["slug"]

        page = WebsitePage.objects.filter(
            slug=slug,
            is_active=True,
        ).first()

        context["page"] = page

        return context

#-------HomeHero----------------------------------
class HomeHeroListView(LoginRequiredMixin, TemplateView):
    template_name = "website/hero_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heroes"] = HomeHero.objects.all()
        return context


class HomeHeroCreateView(LoginRequiredMixin, TemplateView):
    template_name = "website/hero_form.html"

    def get(self, request, *args, **kwargs):
        form = HomeHeroForm()
        return self.render_to_response({
            "form": form,
            "title": "Add Hero Slide",
        })

    def post(self, request, *args, **kwargs):
        form = HomeHeroForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("hero_list")

        return self.render_to_response({
            "form": form,
            "title": "Add Hero Slide",
        })


class HomeHeroUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "website/hero_form.html"

    def get(self, request, *args, **kwargs):
        hero = HomeHero.objects.get(id=kwargs["id"])
        form = HomeHeroForm(instance=hero)

        return self.render_to_response({
            "form": form,
            "title": "Edit Hero Slide",
            "hero": hero,
        })

    def post(self, request, *args, **kwargs):
        hero = HomeHero.objects.get(id=kwargs["id"])
        form = HomeHeroForm(
            request.POST,
            request.FILES,
            instance=hero,
        )

        if form.is_valid():
            form.save()
            return redirect("hero_list")

        return self.render_to_response({
            "form": form,
            "title": "Edit Hero Slide",
            "hero": hero,
        })


class HomeHeroDeleteView(LoginRequiredMixin, TemplateView):
    template_name = "website/hero_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        hero = HomeHero.objects.get(id=kwargs["id"])
        return self.render_to_response({"hero": hero})

    def post(self, request, *args, **kwargs):
        hero = HomeHero.objects.get(id=kwargs["id"])
        hero.delete()
        return redirect("hero_list")


class AboutSectionView(LoginRequiredMixin, TemplateView):
    template_name = "website/about_form.html"

    def get(self, request, *args, **kwargs):
        about = AboutSection.objects.first()
        form = AboutSectionForm(instance=about)

        return self.render_to_response({
            "form": form,
            "about": about,
        })

    def post(self, request, *args, **kwargs):
        about = AboutSection.objects.first()

        form = AboutSectionForm(
            request.POST,
            request.FILES,
            instance=about,
        )

        if form.is_valid():
            form.save()
            return redirect("about_management")

        return self.render_to_response({
            "form": form,
            "about": about,
        })
