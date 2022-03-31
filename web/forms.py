from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your full name",'class':"form-input"}),
            'phone':TextInput(attrs={'placeholder':"Add phone number",'class':"form-input"}),
            'email':EmailInput(attrs={'placeholder':"Enter email address",'class':"form-input"}),
            'subject':TextInput(attrs={'placeholder':"Select Subject",'class':"form-input"}),
            'message':Textarea(attrs={'class':'form-control','placeholder':"Enter messages",'class':"form-textarea"}),
         }
