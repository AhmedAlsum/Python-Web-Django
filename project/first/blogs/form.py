from django import forms
from .models import SignUp


class Contact_form(forms.Form):
    full_name= forms.CharField(required=False)
    email = forms.EmailField()
    message =forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','full_name']



    def clean_email(self):
        email= self.cleaned_data.get('email')
        emailbase, provider= email.split('@')
        domain , extension = provider.split('.')
        if not extension == 'gov':
            raise forms.ValidationError('please enter .gov domain')
        return email

    def clean_name(self):
        full_name= self.cleaned_data.get('full_name')
        return full_name

