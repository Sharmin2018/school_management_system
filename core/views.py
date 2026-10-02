from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from admission.models import AdmissionApplication
from members.models import Student
from teachers.models import Teacher
from staffs.models import Staff
from departments.models import Department
from notices.models import Notice
from django.shortcuts import redirect
from website.models import WebsiteSettings, NavigationMenu
from website.forms import WebsiteSettingsForm, NavigationMenuForm

# -------------------------
# Dashboard View
# -------------------------

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard.html"
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["application"] = AdmissionApplication.objects.count()

        context["student_count"] = Student.objects.count()

        context["male_students"] = Student.objects.filter(
        gender="Male"
        ).count()

        context["female_students"] = Student.objects.filter(
        gender="Female"
         ).count()

        context["photo_students"] = Student.objects.exclude(
        photo=""
        ).count()

        context["teacher_count"] = Teacher.objects.count()

        context["male_teachers"] = Teacher.objects.filter(
        gender="Male"
        ).count()

        context["female_teachers"] = Teacher.objects.filter(
        gender="Female"
         ).count()

        context["staff_count"] = Staff.objects.count()

        context["male_staffs"] = Staff.objects.filter(
        gender="Male"
        ).count()

        context["female_staffs"] = Staff.objects.filter(
        gender="Female"
         ).count()

        context["department_count"] = Department.objects.count()

        context["notice_count"] = Notice.objects.count()

        context["latest_students"] = Student.objects.order_by("-id")[:5]

        context["latest_teachers"] = Teacher.objects.order_by("-id")[:5]

        context["latest_notices"] = Notice.objects.order_by("-publish_date")[:5]

        return context

# -------------------------
# Website Management View
# -------------------------

class WebsiteManagementView(LoginRequiredMixin, TemplateView):

    template_name = "website_management.html"

# -------------------------
# Website General Settings
# -------------------------

class WebsiteSettingsView(
    LoginRequiredMixin,
    TemplateView,
):

    template_name = "website_settings.html"

    def get(self, request, *args, **kwargs):

        settings = WebsiteSettings.objects.first()

        form = WebsiteSettingsForm(
            instance=settings
        )

        return self.render_to_response(
            {
                "form": form,
                "settings": settings,
            }
        )

    def post(self, request, *args, **kwargs):

        settings = WebsiteSettings.objects.first()

        form = WebsiteSettingsForm(
            request.POST,
            request.FILES,
            instance=settings,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "website_settings"
            )

        return self.render_to_response(
            {
                "form": form,
                "settings": settings,
            }
        )

 # -------------------------
# Navigation Management
# -------------------------

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