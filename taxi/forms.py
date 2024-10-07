from django import forms

from taxi.models import Car, Driver
from taxi.validators import validate_license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        label="Driver's License",
        validators=[validate_license_number],
    )

    class Meta:
        model = Driver
        fields = ("license_number",)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(),
        }
