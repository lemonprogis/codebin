from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='User',max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('Fix username')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Fix username')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('fix email')

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('fix password')



class MsgPostForm(forms.Form):
    title = forms.CharField(label='Title',widget=forms.TextInput(attrs=
        {'size':30,'max_length':30}))
    content = forms.CharField(label='Content',widget=forms.Textarea(attrs={'size':10000}))