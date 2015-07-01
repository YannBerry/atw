from django import forms
from django.forms import ModelForm # TextInput, Textarea, NumberInput, ClearableFileInput
from django.utils.translation import ugettext_lazy as _
#from leaflet.forms.widgets import LeafletWidget
from .models import *

class AddInitiativeForm(ModelForm): # ModelForm if it depends on a model, forms.Form otherwise
    required_css_class = 'required'

    coordinates = forms.CharField(label=_("Click on the map to show where you're anaerobic digester is located"), max_length=200, required=True)
    stage = forms.ModelChoiceField(widget=forms.Select(), queryset=Stage.objects, empty_label="----------")
    status = forms.ModelChoiceField(queryset=Status.objects, empty_label="----------")
    start = forms.DateField()

    class Meta:
        model = Initiative
        fields = ['coordinates', 'stage', 'status', 'project_name','project_leader', 'picture', 'description', 'nbr_installations', 'power', 'start', 'email_validation', 'email']
    
    def clean(self): # allows me to custom the validator of the form
        cleaned_data = super(AddInitiativeForm, self).clean()
        email_validation = cleaned_data.get("email_validation")
        email = cleaned_data.get("email")

        if email_validation and not email:
            msg = _("Must add your valid email.")
            self.add_error('email', msg)
