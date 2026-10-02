from django import forms
from .models import WebsiteSettings, NavigationMenu


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
                    "placeholder": "Menu name",
                }
            ),

            "url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "/about/",
                }
            ),

            "parent": forms.Select(
                attrs={
                    "class": "form-select",
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

            "open_new_tab": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }