from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#No estoy seguro porque se llaman a los emails

#Form de creacion de usuario. Se usa dentro dentro de la pagina de Registro
#Se utiliza la libreria UserCreationForm de DJango para facilitar la vida
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Form de actualización de Usuario
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

#Form de actualización de Perfil de usuario
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

