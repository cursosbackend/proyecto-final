from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"class": "w-full border rounded px-3 py-2 focus:ring-indigo-500 focus:border-indigo-500"}),
            "email": forms.EmailInput(attrs={"class": "w-full border rounded px-3 py-2 focus:ring-indigo-500 focus:border-indigo-500"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ("password1", "password2"):
            self.fields[field_name].widget.attrs.update({
                "class": "w-full border rounded px-3 py-2 focus:ring-indigo-500 focus:border-indigo-500"
            })
