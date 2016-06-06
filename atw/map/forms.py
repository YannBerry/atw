from django import forms
from django.forms import ModelForm # TextInput, Textarea, NumberInput, ClearableFileInput
from django.utils.translation import ugettext_lazy as _
#from leaflet.forms.widgets import LeafletWidget
from .models import *

class AddTripStageForm(ModelForm): # ModelForm if it depends on a model, forms.Form otherwise
    required_css_class = 'required'

    coordinates = forms.CharField(label=_("Click on the map to show where your trip stage is located"), max_length=200, required=True)
    massif = forms.ModelChoiceField(widget=forms.Select(), queryset=Massif.objects, empty_label="----------", label=_("Massif"), required=False)
    type = forms.ModelChoiceField(queryset=Type.objects, empty_label="----------", label=_("Type"))
    trips = forms.ModelMultipleChoiceField(queryset=Trip.objects, label=_("Trips"))
    date = forms.DateField(label=_("Date"))

    class Meta:
        model = TripStage
        fields = ['coordinates', 'stage_name', 'date', 'massif', 'type', 'trips', 'picture_tag', 'story', 'distance', 'duration', 'email_validation', 'email']

    def clean(self): # allows me to custom the validator of the form
        cleaned_data = super(AddTripStageForm, self).clean()
        email_validation = cleaned_data.get("email_validation")
        email = cleaned_data.get("email")

        if email_validation and not email:
            msg = _("Must add your valid email.")
            self.add_error('email', msg)