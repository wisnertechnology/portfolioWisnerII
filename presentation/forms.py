from django import forms
from .models import Mesaj

class formsMesaj(forms.ModelForm):

    Fullname = forms.CharField(label='Nom Complet',  required=True, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"name",
            "placeholder":"Entrer votre nom ",
            "name":"Fullname",
            "type":"text"
        }
    ))

    EmailAddress = forms.CharField(label='Adresse email', required=True, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"email",
            "placeholder":"nom@example.com",
            "name":"EmailAddress",
            "type":"email"
        }
    ))

    PhoneNumber = forms.CharField(label='Numero de telephone', required=True, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"phone",
            "placeholder":"(509) 456-78909",
            "name":"PhoneNumber",
            "type":"phone"
        }
    ))

    
    Message = forms.CharField(label='Laissez-nous un message', required=True, widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "id":"message",
            "placeholder":"Entrer votre message ici...",
            "name":"Message",
            "type":"text",
            'rows':7,
            'cols':20
        }
    ))

    

    class Meta:
        model = Mesaj
        #fields = '__all__'
        fields = ('Fullname','EmailAddress','PhoneNumber','Message')