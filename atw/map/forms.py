from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ClearableFileInput
#from leaflet.forms.widgets import LeafletWidget
from .models import *

class AddInitiativeForm(ModelForm): #ModelForm ou forms.Form
	error_css_class = 'error'
	required_css_class = 'required'

	coordinates = forms.CharField(label="Click on the map to show where you're anaerobic digester is located", max_length=200, required=True)
	stage = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "form-control"}), queryset=Stage.objects, empty_label="----------", required=True)
	status = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "form-control"}), queryset=Status.objects, empty_label="----------", required=True)
	start = forms.DateField()

	class Meta:
		model = Initiative
		fields = ['coordinates', 'stage', 'status', 'project_name','project_leader', 'picture', 'description', 'nbr_installations', 'power', 'start']
		