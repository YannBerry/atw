from django import forms
from django.forms import ModelForm # TextInput, Textarea, NumberInput, ClearableFileInput
from django.utils.translation import ugettext_lazy as _
#from leaflet.forms.widgets import LeafletWidget
from .models import *


class AddTripStageForm(ModelForm):  # ModelForm if it depends on a model, forms.Form otherwise
    # Customize the css of the required fields
    required_css_class = 'required'

    # Redefining the fields to be able to alter their default css
    stage_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Nom de l'étape"))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), label=_("Date"))
    stage_slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Slug"))
    #picture_tag = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), label=_("Photo Principale"))
    story = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label=_("Récit"))
    distance = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label=_("Distance"))
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label=_("Durée"))
    email_validation = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), label=_("Recevoir une validation par e-mail ?"))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label=_("Adresse E-mail"))

    coordinates = forms.CharField(label=_("Cliquer sur le lieu de votre aventure."), max_length=200, required=True)
    massif = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Massif.objects, empty_label="----------", label=_("Massif"))
    type = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Type.objects, empty_label="----------", label=_("Type"))
    trip_linked = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Trip.objects, empty_label="----------", label=_("Aventures liées"))
    country = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Country.objects, empty_label="----------", label=_("Pays"))

    class Meta:
        model = TripStage
        fields = ['coordinates', 'stage_name', 'date', 'massif', 'type', 'country', 'stage_slug', 'trip_linked', 'story', 'distance', 'duration', 'email_validation', 'email']

    # Customize the validator of the form
    def clean(self):
        cleaned_data = super(AddTripStageForm, self).clean()
        email_validation = cleaned_data.get("email_validation")
        email = cleaned_data.get("email")

        if email_validation and not email:
            msg = _("Votre email ne doit pas être valide.")
            self.add_error('email', msg)
