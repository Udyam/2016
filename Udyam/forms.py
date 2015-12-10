from django import forms
from models import Team


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Team()
        fields = '__all__'
