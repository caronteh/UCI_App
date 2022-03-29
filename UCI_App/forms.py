from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}




DEMO_CHOICES = (
    ("Ninguna me convence", "Ninguna me convence"),
    ("Bajar VT", "Bajar VT"),
    ("Bajar PEEP", "Bajar PEEP"),
    ("Bajar RR", "Bajar RR"),
)


class PropuestasForm(forms.Form):

    Propuestas = forms.MultipleChoiceField(choices=DEMO_CHOICES, label='')














class MapasHitsForm(forms.Form):

    Opciones = forms.CharField(label='')

class EySForm(forms.Form):

    EyS = forms.IntegerField(label='')


