from django.core import validators
from django import forms
from django.forms import fields, widgets
from .models import Residence

class ResidenceRegistration(forms.ModelForm):
    class Meta:
        model = Residence
        fields = ['image', 'nomResidence', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'nomResidence': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }