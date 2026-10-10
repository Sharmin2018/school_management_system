from django import forms

from .models import (
    WebsiteSettings,
    NavigationMenu,
    WebsitePage,
    HomeHero,
    AboutSection,
    SchoolStatistic,
)


class WebsiteSettingsForm(forms.ModelForm):

    class Meta:
        model = WebsiteSettings

        fields = [
            "logo",
            "address",
            "phone",
            "email",
        ]

        widgets = {
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class NavigationMenuForm(forms.ModelForm):
    class Meta:
        model = NavigationMenu
        fields = [
            "name",
            "page",
            "url",
            "parent",
            "order",
            "is_active",
            "open_new_tab",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Menu name"
                }
            ),

            "page": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "/admission/ or https://example.com/"
                }
            ),

            "parent": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "order": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),

            "open_new_tab": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }

class WebsitePageForm(forms.ModelForm):
    class Meta:
        model = WebsitePage
        fields = [
            "title",
            "slug",
            "content",
            "image",
            "is_active",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Page title",
                }
            ),

            "slug": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "about",
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "Write page content...",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

class HomeHeroForm(forms.ModelForm):
    class Meta:
        model = HomeHero
        fields = [
            "title",
            "subtitle",
            "description",
            "background_image",
            "button_text",
            "button_url",
            "order",
            "is_active",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Hero title",
                }
            ),

            "subtitle": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Hero subtitle",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Hero description...",
                }
            ),

            "background_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "button_text": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Button text",
                }
            ),

            "button_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "/about/",
                }
            ),

            "order": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = [
            "title",
            "short_description",
            "image",
            "button_text",
            "button_url",
            "is_active",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "short_description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            "button_text": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "button_url": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }


class SchoolStatisticForm(forms.ModelForm):
    class Meta:
        model = SchoolStatistic
        fields = [
            "title",
            "value",
            "icon",
            "order",
            "is_active",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. Total Students",
            }),
            "value": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
            }),
            "icon": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "bi-people-fill",
            }),
            "order": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }

