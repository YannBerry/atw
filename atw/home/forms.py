from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        # widgets = {
        # 	'username': TextInput(attrs={"placeholder": "Username", "class": "form-control"}),
        # 	'email': TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
        # 	'password1': TextInput(attrs={"placeholder": "Password", "class": "form-control"}),
        # 	'password2': TextInput(attrs={"placeholder": "Password confirmation", "class": "form-control"}),
        # }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user