from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from models import *
from w_enums import *

class MessageForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    language = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=LANGUAGES)

    class Meta:
        model = Message
        fields = ('title', 'content', 'language')

    def customSave(self,user):
        lv = self.save(commit=False)
        lv.user = user
        lv.save()
        return lv

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        

class UserLoginForm(forms.Form):
    pass

