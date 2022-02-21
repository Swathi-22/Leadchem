
from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'class':'required form-control','placeholder':"Name"}),
            'phone':TextInput(attrs={'class':'required form-control','placeholder':"Phone"}),
            'email':EmailInput(attrs={'class':'required form-control','placeholder':"Email"}),
            'message':Textarea(attrs={'class':'form-control','placeholder':"your message",'row':'10'}),
         }
